import sys
import unittest
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile
from io import BytesIO
from xml.etree import ElementTree

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from main import app
from app.pages import render_page


FB2 = b'''<?xml version="1.0" encoding="UTF-8"?>
<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0"><description><title-info><book-title>Test</book-title></title-info></description><body><section><p>Hello</p></section></body></FictionBook>'''


class WebsiteTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_guide_button_diagram(self):
        for language in ("ru", "en"):
            page = render_page(language, "guide").decode("utf-8")
            start = page.index('<svg class="x3-diagram"')
            end = page.index("</svg>", start) + len("</svg>")
            svg = ElementTree.fromstring(page[start:end])
            self.assertEqual(len(svg.findall(".//{http://www.w3.org/2000/svg}circle")), 4)
            self.assertIn('M352 148h-5v42h5M588 148h5v42h-5', page)
            self.assertIn('M605 509H580L506 432', page)
            self.assertIn('M710 82H650V18H533V30', page)
            self.assertNotIn('class="diagram-label">→', page)
            self.assertNotIn('class="diagram-label">←', page)
            if language == "ru":
                self.assertIn('class="diagram-label">ВОЗВРАТ', page)
                self.assertIn('class="diagram-label">ВЫБОР', page)

    def test_pages_and_health(self):
        self.assertIn("PagePet Reader", self.client.get("/").text)
        self.assertIn('<html lang="en">', self.client.get("/en").text)
        self.assertIn("Сборки пока готовятся", self.client.get("/downloads").text)
        guide_ru = self.client.get("/guide")
        guide_en = self.client.get("/en/guide")
        self.assertEqual(guide_ru.status_code, 200)
        self.assertIn("От файла до первой страницы", guide_ru.text)
        self.assertIn("Кнопки во время чтения", guide_ru.text)
        self.assertIn('class="x3-diagram"', guide_ru.text)
        self.assertNotIn("Нижний ряд —", guide_ru.text)
        self.assertIn("Размер текста", guide_ru.text)
        self.assertEqual(guide_en.status_code, 200)
        self.assertIn("From file to first page", guide_en.text)
        self.assertNotIn("X3 front view · button map", guide_en.text)
        self.assertNotIn("Bottom row —", guide_en.text)
        self.assertIn('href="/en/guide"', self.client.get("/en").text)
        self.assertIn('name="format"', self.client.get("/convert").text)
        self.assertEqual(self.client.get("/healthz").json(), {"status": "ok"})

    def test_upload_returns_epub(self):
        def fake_convert(source, output):
            with ZipFile(output, "w") as archive:
                archive.writestr("mimetype", "application/epub+zip")

        with patch("app.routes.conversion.convert_book", side_effect=fake_convert):
            response = self.client.post("/api/convert", files={"file": ("book.fb2", FB2)}, data={"format": "epub"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["content-type"], "application/epub+zip")
        with ZipFile(BytesIO(response.content)) as archive:
            self.assertEqual(archive.read("mimetype"), b"application/epub+zip")

    def test_rejects_pdf_and_same_format(self):
        pdf = self.client.post("/api/convert", files={"file": ("book.pdf", b"bad")}, data={"format": "epub"})
        self.assertEqual(pdf.status_code, 400)
        self.assertIn("не поддерживается", pdf.json()["detail"])
        same = self.client.post("/api/convert?lang=en", files={"file": ("book.epub", b"book")}, data={"format": "epub"})
        self.assertEqual(same.status_code, 400)
        self.assertIn("different", same.json()["detail"])


if __name__ == "__main__":
    unittest.main()
