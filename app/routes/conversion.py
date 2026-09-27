"""Book upload and conversion endpoint."""

from __future__ import annotations

import asyncio
from pathlib import Path
import sys
import tempfile
from threading import BoundedSemaphore
from urllib.parse import quote

from fastapi import APIRouter, File, Form, HTTPException, Query, UploadFile
from fastapi.responses import Response

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "converter-core"))
from pagepet_converter import ConversionError, INPUT_FORMATS, OUTPUT_FORMATS, convert_book  # noqa: E402


router = APIRouter()
MAX_FILE_BYTES = 20 * 1024 * 1024
MAX_OUTPUT_BYTES = 40 * 1024 * 1024
CONVERSIONS = BoundedSemaphore(2)
MIME_TYPES = {
    "epub": "application/epub+zip",
    "fb2": "application/xml",
    "mobi": "application/x-mobipocket-ebook",
    "azw3": "application/vnd.amazon.ebook",
    "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "txt": "text/plain",
}
MESSAGES = {
    "ru": {
        "source": "Этот формат файла не поддерживается",
        "target": "Формат результата не поддерживается",
        "same": "Выберите другой формат результата",
        "size": "Файл пустой или больше 20 МБ",
        "busy": "Сервис занят. Попробуйте чуть позже",
        "failed": "Не удалось конвертировать книгу",
        "timeout": "Время конвертации истекло",
        "missing": "Calibre не установлен на сервере",
        "output": "Результат слишком большой",
    },
    "en": {
        "source": "This input format is not supported",
        "target": "This output format is not supported",
        "same": "Choose a different output format",
        "size": "The file is empty or larger than 20 MB",
        "busy": "The converter is busy. Try again shortly",
        "failed": "The book could not be converted",
        "timeout": "Conversion timed out",
        "missing": "Calibre is not installed on the server",
        "output": "The converted file is too large",
    },
}


def error(language: str, key: str, status: int) -> HTTPException:
    return HTTPException(status_code=status, detail=MESSAGES[language][key])


@router.post("/api/convert")
async def convert(
    file: UploadFile = File(...),
    format: str = Form(...),
    lang: str = Query("ru"),
) -> Response:
    language = "en" if lang == "en" else "ru"
    filename = Path(file.filename or "").name
    source_format = Path(filename).suffix.lower().removeprefix(".")
    target_format = format.lower()
    if source_format not in INPUT_FORMATS:
        raise error(language, "source", 400)
    if target_format not in OUTPUT_FORMATS:
        raise error(language, "target", 400)
    if source_format == target_format:
        raise error(language, "same", 400)
    if not CONVERSIONS.acquire(blocking=False):
        raise error(language, "busy", 503)

    try:
        data = await file.read(MAX_FILE_BYTES + 1)
        if not data or len(data) > MAX_FILE_BYTES:
            raise error(language, "size", 413)
        with tempfile.TemporaryDirectory(prefix="pagepet-request-") as directory:
            source = Path(directory) / f"input.{source_format}"
            output = Path(directory) / f"output.{target_format}"
            source.write_bytes(data)
            try:
                await asyncio.to_thread(convert_book, source, output)
            except ConversionError as exc:
                key = {"Calibre is not installed": "missing", "Conversion timed out": "timeout"}.get(str(exc), "failed")
                raise error(language, key, 422) from exc
            if output.stat().st_size > MAX_OUTPUT_BYTES:
                raise error(language, "output", 413)
            result = output.read_bytes()
        download_name = (Path(filename).stem or "book") + f".{target_format}"
        return Response(
            result,
            media_type=MIME_TYPES[target_format],
            headers={"Content-Disposition": f"attachment; filename=book.{target_format}; filename*=UTF-8''{quote(download_name)}", "Cache-Control": "no-store"},
        )
    finally:
        CONVERSIONS.release()
