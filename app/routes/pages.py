"""Page and asset routes."""

from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, Response, FileResponse

from app.pages import render_page


router = APIRouter()
STATIC = Path(__file__).resolve().parents[2] / "static"


@router.get("/healthz")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/", response_class=HTMLResponse)
@router.get("/downloads", response_class=HTMLResponse)
@router.get("/convert", response_class=HTMLResponse)
@router.get("/en", response_class=HTMLResponse)
@router.get("/en/downloads", response_class=HTMLResponse)
@router.get("/en/convert", response_class=HTMLResponse)
def page_route(request: Request) -> Response:
    path = request.url.path
    language = "en" if path == "/en" or path.startswith("/en/") else "ru"
    name = path.removeprefix("/en").strip("/") or "home"
    return HTMLResponse(render_page(language, name))


@router.get("/style.css")
def style() -> FileResponse:
    return FileResponse(STATIC / "style.css", media_type="text/css")


@router.get("/app.js")
def script() -> FileResponse:
    return FileResponse(STATIC / "app.js", media_type="text/javascript")


@router.get("/dragon.png")
def dragon() -> FileResponse:
    return FileResponse(STATIC / "dragon.png", media_type="image/png")
