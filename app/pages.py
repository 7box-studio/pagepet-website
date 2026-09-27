"""Russian and English pages for the PagePet website."""

from __future__ import annotations

from html import escape


COPY = {
    "ru": {
        "nav_downloads": "Прошивка",
        "nav_convert": "Конвертер",
        "nav_about": "О PagePet",
        "home_title": "PagePet Reader",
        "home_intro": "Готовим прошивку для Xteink X3 и X4. Читайте книги, а маленький дракончик будет расти вместе с вашим прогрессом.",
        "home_action": "Прошивка и установка",
        "home_secondary": "Подготовить книгу",
        "home_status": "PagePet Reader ещё в разработке. Проверенные сборки появятся на странице прошивки.",
        "feature_title": "Что мы делаем",
        "feature_1_title": "Чтение на первом месте",
        "feature_1": "Книги, удобная навигация и настройки текста — основа прошивки.",
        "feature_2_title": "Спутник рядом",
        "feature_2": "Дракончик замечает ваш прогресс. Его можно оставить в стороне, когда хочется просто читать.",
        "feature_3_title": "Книги без лишних шагов",
        "feature_3": "Преобразуйте книгу в EPUB прямо на сайте и перенесите файл на читалку.",
        "downloads_title": "Прошивка для Xteink",
        "downloads_intro": "Здесь будут сборки PagePet Reader и инструкции по установке для каждой проверенной модели.",
        "downloads_notice_title": "Сборки пока готовятся",
        "downloads_notice": "Мы ещё проверяем прошивку на устройствах. Скачивание откроем после этих тестов — сейчас устанавливать PagePet Reader рано.",
        "device_status": "Проверка в работе",
        "device_x3": "Xteink X3",
        "device_x4": "Xteink X4",
        "downloads_follow": "Следить за разработкой",
        "downloads_source": "Исходный код",
        "downloads_next_title": "Перед установкой",
        "downloads_next": "Для каждой сборки опубликуем версию устройства, файл прошивки, контрольную сумму и шаги восстановления. Не используйте файл от другой модели.",
        "convert_title": "Конвертер книг",
        "convert_intro": "Выберите книгу и формат результата. Для PagePet Reader обычно подходит EPUB.",
        "select_file": "Выбрать книгу",
        "drop_file": "или перетащить сюда",
        "limit": "EPUB, FB2, MOBI, AZW3, DOCX, TXT, RTF, ODT · до 20 МБ",
        "output_label": "Формат результата",
        "convert_button": "Конвертировать",
        "convert_idle": "После обработки файл удаляется с сервера.",
        "convert_working": "Конвертируем книгу…",
        "convert_success": "Готово. Файл скачан на ваше устройство.",
        "convert_missing": "Сначала выберите книгу.",
        "convert_invalid": "Проверьте формат и размер файла (до 20 МБ).",
        "convert_same": "Выберите другой формат результата.",
        "convert_failed": "Не удалось конвертировать книгу.",
        "convert_usage_title": "Как перенести книгу",
        "convert_usage": "Скачайте файл и скопируйте его на SD-карту читалки.",
        "footer_status": "Сайт и прошивка в разработке",
        "footer_channel": "Новости проекта",
        "footer_code": "Исходный код",
    },
    "en": {
        "nav_downloads": "Firmware",
        "nav_convert": "Converter",
        "nav_about": "About PagePet",
        "home_title": "PagePet Reader",
        "home_intro": "We're making firmware for the Xteink X3 and X4. Read your books while a small dragon grows alongside your progress.",
        "home_action": "Firmware and installation",
        "home_secondary": "Prepare a book",
        "home_status": "PagePet Reader is in development. Tested builds will appear on the firmware page.",
        "feature_title": "What we're building",
        "feature_1_title": "Reading comes first",
        "feature_1": "Books, clear navigation, and text settings are the foundation of the firmware.",
        "feature_2_title": "A companion nearby",
        "feature_2": "The dragon follows your progress. You can leave it aside when you just want to read.",
        "feature_3_title": "Books, ready to go",
        "feature_3": "Convert a book to EPUB on this website, then move it to your reader.",
        "downloads_title": "Firmware for Xteink",
        "downloads_intro": "Tested PagePet Reader builds and installation instructions for each device will appear here.",
        "downloads_notice_title": "Builds are in progress",
        "downloads_notice": "We are still testing the firmware on devices. Downloads will open after those checks; PagePet Reader is not ready to install yet.",
        "device_status": "Testing in progress",
        "device_x3": "Xteink X3",
        "device_x4": "Xteink X4",
        "downloads_follow": "Follow development",
        "downloads_source": "Source code",
        "downloads_next_title": "Before installing",
        "downloads_next": "Each build will include the device version, firmware file, checksum, and recovery steps. Do not flash a file for another model.",
        "convert_title": "Book converter",
        "convert_intro": "Choose a book and an output format. EPUB usually works best for PagePet Reader.",
        "select_file": "Choose a book",
        "drop_file": "or drop it here",
        "limit": "EPUB, FB2, MOBI, AZW3, DOCX, TXT, RTF, ODT · up to 20 MB",
        "output_label": "Output format",
        "convert_button": "Convert book",
        "convert_idle": "The file is removed from the server after processing.",
        "convert_working": "Converting your book…",
        "convert_success": "Done. Your book has been downloaded.",
        "convert_missing": "Choose a book first.",
        "convert_invalid": "Check the format and file size (up to 20 MB).",
        "convert_same": "Choose a different output format.",
        "convert_failed": "The book could not be converted.",
        "convert_usage_title": "Move the book to your reader",
        "convert_usage": "Download the file and copy it to the reader's SD card.",
        "footer_status": "Website and firmware in development",
        "footer_channel": "Project updates",
        "footer_code": "Source code",
    },
}


def _link(language: str, page: str) -> str:
    prefix = "/en" if language == "en" else ""
    suffix = "" if page == "home" else f"/{page}"
    return prefix + suffix or "/"


def _layout(language: str, page: str, body: str) -> bytes:
    t = COPY[language]
    other = "en" if language == "ru" else "ru"
    title = {"home": "PagePet Reader", "downloads": t["nav_downloads"], "convert": t["nav_convert"]}[page]
    nav = "".join(
        f'<a class="{"active" if page == key else ""}" href="{_link(language, key)}">{escape(t[label])}</a>'
        for key, label in (("home", "nav_about"), ("downloads", "nav_downloads"), ("convert", "nav_convert"))
    )
    document = f'''<!doctype html>
<html lang="{language}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#122e37"><title>{escape(title)} — PagePet Reader</title>
<link rel="stylesheet" href="/style.css"><script src="/app.js" defer></script></head>
<body><header class="site-header"><a class="brand" href="{_link(language, 'home')}"><span class="brand-pixel" aria-hidden="true">P</span><span>PagePet Reader</span></a>
<nav aria-label="Navigation">{nav}</nav><a class="language" href="{_link(other, page)}" lang="{other}" aria-label="{'English' if other == 'en' else 'Русский'}">{'EN' if other == 'en' else 'RU'}</a></header>
<main>{body}</main>
<footer><span>PagePet Reader · {escape(t['footer_status'])}</span><div><a href="https://github.com/7box-studio/pagepet-reader">{escape(t['footer_code'])}</a><a href="https://t.me/pagepet_reader">{escape(t['footer_channel'])}</a></div></footer></body></html>'''
    return document.encode("utf-8")


def render_page(language: str, page: str) -> bytes:
    t = COPY[language]
    if page == "home":
        body = f'''<section class="home-hero"><div class="hero-copy"><p class="product-type">PagePet Reader · Xteink X3 / X4</p><h1>{escape(t['home_title'])}</h1><p class="lead">{escape(t['home_intro'])}</p><div class="actions"><a class="button" href="{_link(language, 'downloads')}">{escape(t['home_action'])}<span aria-hidden="true">↗</span></a><a class="secondary-link" href="{_link(language, 'convert')}">{escape(t['home_secondary'])}</a></div><p class="build-status">{escape(t['home_status'])}</p></div><div class="dragon-panel"><img src="/dragon.png" alt="{'Green pixel dragon reading a book' if language == 'en' else 'Зелёный пиксельный дракончик читает книгу'}" width="1254" height="1254"></div></section>
<section class="features"><h2>{escape(t['feature_title'])}</h2><div class="feature-grid">{''.join(f'<article><span class="pixel-icon" aria-hidden="true">{icon}</span><h3>{escape(t[f"feature_{n}_title"])}</h3><p>{escape(t[f"feature_{n}"])}</p></article>' for n, icon in ((1, '▤'), (2, '✦'), (3, '↗')))}</div></section>'''
    elif page == "downloads":
        body = f'''<section class="page-intro"><p class="product-type">PagePet Reader · Xteink X3 / X4</p><h1>{escape(t['downloads_title'])}</h1><p class="lead">{escape(t['downloads_intro'])}</p></section>
<section class="download-section"><div class="notice"><span class="status-dot" aria-hidden="true"></span><div><h2>{escape(t['downloads_notice_title'])}</h2><p>{escape(t['downloads_notice'])}</p></div></div><div class="device-grid">{''.join(f'<article class="device-card"><div class="device-glyph" aria-hidden="true">▣</div><h3>{escape(t[name])}</h3><span>{escape(t["device_status"])}</span></article>' for name in ('device_x3', 'device_x4'))}</div><div class="download-links"><a class="button" href="https://t.me/pagepet_reader">{escape(t['downloads_follow'])}<span aria-hidden="true">↗</span></a><a class="secondary-link" href="https://github.com/7box-studio/pagepet-reader">{escape(t['downloads_source'])}</a></div></section>
<section class="information"><h2>{escape(t['downloads_next_title'])}</h2><p>{escape(t['downloads_next'])}</p></section>'''
    elif page == "convert":
        body = f'''<section class="page-intro"><p class="product-type">EPUB · FB2 · MOBI</p><h1>{escape(t['convert_title'])}</h1><p class="lead">{escape(t['convert_intro'])}</p></section><section class="convert-layout"><form class="converter-card" id="convert-form" data-language="{language}" data-missing="{escape(t['convert_missing'])}" data-invalid="{escape(t['convert_invalid'])}" data-same="{escape(t['convert_same'])}" data-working="{escape(t['convert_working'])}" data-success="{escape(t['convert_success'])}" data-failed="{escape(t['convert_failed'])}" data-button="{escape(t['convert_button'])}" data-select="{escape(t['select_file'])}"><label class="drop-zone" id="drop-zone" for="book-file"><span class="upload-icon" aria-hidden="true">↥</span><strong id="file-label">{escape(t['select_file'])}</strong><span>{escape(t['drop_file'])}</span></label><input id="book-file" name="file" type="file" accept=".epub,.fb2,.mobi,.azw3,.docx,.txt,.rtf,.odt" required><p class="limit">{escape(t['limit'])}</p><div class="format-row"><label for="output-format">{escape(t['output_label'])}</label><select id="output-format" name="format">{''.join(f'<option value="{format_name}">{format_name.upper()}</option>' for format_name in ('epub', 'fb2', 'mobi', 'azw3', 'docx', 'txt'))}</select></div><button class="button convert-button" type="submit">{escape(t['convert_button'])}<span aria-hidden="true">↗</span></button><p id="status" class="status" role="status" aria-live="polite">{escape(t['convert_idle'])}</p></form><aside class="convert-help"><div class="device-glyph" aria-hidden="true">▣</div><h2>{escape(t['convert_usage_title'])}</h2><p>{escape(t['convert_usage'])}</p></aside></section>'''
    else:
        raise ValueError("Unknown page")
    return _layout(language, page, body)
