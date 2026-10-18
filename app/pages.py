"""Russian and English pages for the PagePet website."""

from __future__ import annotations

from html import escape


COPY = {
    "ru": {
        "nav_downloads": "Прошивка",
        "nav_convert": "Конвертер",
        "nav_guide": "Как читать",
        "nav_about": "О PagePet",
        "home_title": "PagePet Reader",
        "home_intro": "Готовим открытую прошивку для Xteink X3. Читайте с физических кнопок, а маленький дракончик будет расти вместе с вашим прогрессом.",
        "home_action": "Прошивка и установка",
        "home_secondary": "Подготовить книгу",
        "home_guide": "Как читать на X3",
        "home_status": "PagePet Reader ещё в разработке. Проверенные сборки появятся на странице прошивки.",
        "feature_title": "Что мы делаем",
        "feature_1_title": "Чтение на первом месте",
        "feature_1": "Книги, удобная навигация и настройки текста — основа прошивки.",
        "feature_2_title": "Спутник рядом",
        "feature_2": "Дракончик замечает ваш прогресс. Его можно оставить в стороне, когда хочется просто читать.",
        "feature_3_title": "Книги без лишних шагов",
        "feature_3": "Подготовьте книгу в TXT и перенесите её на microSD — текущая прошивка читает UTF-8 .txt.",
        "downloads_title": "Прошивка для Xteink X3",
        "downloads_intro": "Здесь появится проверенная сборка PagePet Reader для Xteink X3 и инструкция по установке.",
        "downloads_notice_title": "Сборки пока готовятся",
        "downloads_notice": "Мы ещё проверяем прошивку на устройствах. Скачивание откроем после этих тестов — сейчас устанавливать PagePet Reader рано.",
        "device_status": "Проверка в работе",
        "device_x3": "Xteink X3",
        "downloads_follow": "Следить за разработкой",
        "downloads_source": "Исходный код",
        "downloads_next_title": "Перед установкой",
        "downloads_next": "Для сборки опубликуем версию устройства, файл прошивки, контрольную сумму и шаги восстановления. Не используйте файл от другой модели.",
        "convert_title": "Конвертер книг",
        "convert_intro": "Выберите книгу и формат результата. Для текущей прошивки X3 выбирайте TXT: она читает UTF-8 .txt с корня microSD.",
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
        "convert_usage": "Скачайте TXT и скопируйте его в корень microSD. Другие выходные форматы конвертера текущая прошивка пока не читает.",
        "guide_title": "От файла до первой страницы",
        "guide_intro": "Короткий гид по текущей версии PagePet Reader для Xteink X3. Для чтения нужна книга в UTF-8 TXT и карта microSD.",
        "guide_status": "Прошивка ещё проходит проверку на устройствах. Этот гид описывает текущую сборку для разработки; проверенную версию опубликуем на странице прошивки.",
        "guide_step_1_title": "Подготовьте книгу",
        "guide_step_1": "Если книга уже в UTF-8 TXT, оставьте её как есть. Для другого формата воспользуйтесь конвертером и выберите TXT. В текущей прошивке EPUB и FB2 пока не открываются.",
        "guide_step_2_title": "Перенесите на microSD",
        "guide_step_2": "Скопируйте файл .txt в корень карты, без папок. Сейчас список показывает до 14 книг.",
        "guide_step_3_title": "Откройте и читайте",
        "guide_step_3": "На главном экране выберите книгу кнопками вверх/вниз и нажмите OK. Во время чтения боковые кнопки листают страницы, а OK открывает выбор размера текста.",
        "guide_step_4_title": "Продолжите позже",
        "guide_step_4": "Нажмите «Назад», чтобы вернуться к списку. На главном экране «Назад» открывает последнюю сохранённую книгу. Кнопка питания переводит устройство в сон.",
        "guide_keys_title": "Кнопки во время чтения",
        "guide_diagram_desc": "Схема Xteink X3: боковые клавиши листают страницы; сверху справа питание; снизу слева направо: назад, OK, следующая и предыдущая страницы.",
        "guide_power": "Сон",
        "guide_power_detail": "Питание",
        "guide_prev": "Предыдущая",
        "guide_next": "Следующая",
        "guide_back": "К списку",
        "guide_ok": "Размер текста",
        "guide_key_up": "Назад на страницу",
        "guide_key_down": "Вперёд на страницу",
        "guide_key_ok": "Размер текста",
        "guide_key_back": "К списку книг",
        "guide_note_title": "Если книга не появилась",
        "guide_note": "Проверьте, что карта читается, файл имеет расширение .txt, находится в корне microSD и содержит текст в UTF-8. Папки и другие форматы текущая версия не показывает.",
        "guide_convert": "Подготовить TXT",
        "footer_status": "Сайт и прошивка в разработке",
        "footer_channel": "Новости проекта",
        "footer_code": "Исходный код",
    },
    "en": {
        "nav_downloads": "Firmware",
        "nav_convert": "Converter",
        "nav_guide": "Reading guide",
        "nav_about": "About PagePet",
        "home_title": "PagePet Reader",
        "home_intro": "We're building open firmware for the Xteink X3. Read with physical buttons while a small dragon grows alongside your progress.",
        "home_action": "Firmware and installation",
        "home_secondary": "Prepare a book",
        "home_guide": "How to read on X3",
        "home_status": "PagePet Reader is in development. Tested builds will appear on the firmware page.",
        "feature_title": "What we're building",
        "feature_1_title": "Reading comes first",
        "feature_1": "Books, clear navigation, and text settings are the foundation of the firmware.",
        "feature_2_title": "A companion nearby",
        "feature_2": "The dragon follows your progress. You can leave it aside when you just want to read.",
        "feature_3_title": "Books, ready to go",
        "feature_3": "Prepare a book as TXT, then move it to the reader's microSD card — the current firmware reads UTF-8 .txt files.",
        "downloads_title": "Firmware for Xteink X3",
        "downloads_intro": "A tested PagePet Reader build for the Xteink X3 and its installation guide will appear here.",
        "downloads_notice_title": "Builds are in progress",
        "downloads_notice": "We are still testing the firmware on devices. Downloads will open after those checks; PagePet Reader is not ready to install yet.",
        "device_status": "Testing in progress",
        "device_x3": "Xteink X3",
        "downloads_follow": "Follow development",
        "downloads_source": "Source code",
        "downloads_next_title": "Before installing",
        "downloads_next": "Each build will include the device version, firmware file, checksum, and recovery steps. Do not flash a file for another model.",
        "convert_title": "Book converter",
        "convert_intro": "Choose a book and an output format. For the current X3 firmware, choose TXT: it reads UTF-8 .txt files from the microSD root.",
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
        "convert_usage": "Download the TXT file and copy it to the microSD root. The current firmware does not yet read the converter's other output formats.",
        "guide_title": "From file to first page",
        "guide_intro": "A short guide to the current PagePet Reader build for Xteink X3. You need a UTF-8 TXT book and a microSD card.",
        "guide_status": "The firmware is still being tested on devices. This guide describes the development build; a tested release will appear on the firmware page.",
        "guide_step_1_title": "Prepare the book",
        "guide_step_1": "If you already have a UTF-8 TXT file, keep it. For another format, use the converter and choose TXT. The current firmware does not open EPUB or FB2 yet.",
        "guide_step_2_title": "Copy it to microSD",
        "guide_step_2": "Put the .txt file in the card root, outside folders. The current list shows up to 14 books.",
        "guide_step_3_title": "Open and read",
        "guide_step_3": "On Home, select a book with Up/Down and press OK. While reading, the side buttons turn pages; OK opens text size settings.",
        "guide_step_4_title": "Pick up later",
        "guide_step_4": "Press Back to return to the book list. On Home, Back opens the last saved book. The power button puts the reader to sleep.",
        "guide_keys_title": "Buttons while reading",
        "guide_diagram_desc": "Xteink X3 diagram: side buttons turn pages; power is at the top right; bottom buttons from left to right are Back, OK, Next page, Previous page.",
        "guide_power": "Sleep",
        "guide_power_detail": "Power",
        "guide_prev": "Previous",
        "guide_next": "Next",
        "guide_back": "Book list",
        "guide_ok": "Text size",
        "guide_key_up": "Previous page",
        "guide_key_down": "Next page",
        "guide_key_ok": "Text size",
        "guide_key_back": "Book list",
        "guide_note_title": "If the book does not appear",
        "guide_note": "Check that the card is readable, the file ends in .txt, sits in the microSD root, and contains UTF-8 text. This build does not list folders or other formats.",
        "guide_convert": "Prepare a TXT file",
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
    title = {"home": "PagePet Reader", "downloads": t["nav_downloads"], "convert": t["nav_convert"], "guide": t["nav_guide"]}[page]
    nav = "".join(
        f'<a class="{"active" if page == key else ""}" href="{_link(language, key)}">{escape(t[label])}</a>'
        for key, label in (("home", "nav_about"), ("guide", "nav_guide"), ("downloads", "nav_downloads"), ("convert", "nav_convert"))
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


def _device_diagram(t: dict[str, str]) -> str:
    """X3 front view. Physical button positions: official X3 User Guide, page 3."""
    label = lambda key: escape(t[key])
    return f'''<section class="guide-diagram" aria-labelledby="guide-diagram-heading">
<div class="guide-diagram-heading"><p class="guide-screen-label">DEVICE / 01</p><h2 id="guide-diagram-heading">{label('guide_keys_title')}</h2></div>
<div class="guide-diagram-scroll"><svg class="x3-diagram" viewBox="0 0 940 590" role="img" aria-labelledby="x3-title x3-desc" xmlns="http://www.w3.org/2000/svg">
<title id="x3-title">{label('guide_keys_title')}</title><desc id="x3-desc">{label('guide_diagram_desc')}</desc>
<defs><marker id="guide-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M1 1 7 4.5 1 8" fill="none" stroke="#285f4a" stroke-width="1.6"/></marker></defs>
<g class="diagram-device">
<rect x="356" y="38" width="228" height="412" rx="20" fill="#c9cbc7" stroke="#20353b" stroke-width="3"/>
<rect x="364" y="46" width="212" height="396" rx="15" fill="none" stroke="#9da6a1" stroke-width="2"/>
<rect x="376" y="65" width="188" height="320" rx="5" fill="#f5f3e9" stroke="#778780" stroke-width="2"/>
<text x="393" y="94" class="device-screen-title">PagePet Reader</text>
<path d="M393 114h151M393 129h139M393 144h149M393 159h119M393 192h150M393 207h128M393 222h146M393 237h136M393 270h148M393 285h133M393 300h144M393 315h103" stroke="#a5aaa4" stroke-width="3" stroke-linecap="round"/>
<path d="M352 148h-5v42h5M588 174h5v42h-5M519 34v-4h28v4" fill="#aeb8b0" stroke="#20353b" stroke-width="2"/>
<rect x="395" y="410" width="83" height="13" rx="6" fill="#e0e2dc" stroke="#78827e" stroke-width="1.5"/>
<rect x="486" y="410" width="83" height="13" rx="6" fill="#e0e2dc" stroke="#78827e" stroke-width="1.5"/>
<path d="M436.5 411v11M527.5 411v11" stroke="#87948c" stroke-width="1.3"/>
<circle cx="415" cy="416.5" r="3" fill="#285f4a"/><circle cx="457" cy="416.5" r="3" fill="#285f4a"/><circle cx="506" cy="416.5" r="3" fill="#285f4a"/><circle cx="548" cy="416.5" r="3" fill="#285f4a"/>
</g>
<g class="diagram-lines" fill="none" stroke="#285f4a" stroke-width="2" marker-end="url(#guide-arrow)">
<path d="M234 179H341"/><path d="M705 202H603"/><path d="M710 82H594L546 35"/>
<path d="M148 509H350L415 432"/><path d="M338 543H399L457 432"/>
<path d="M605 509H580L506 432"/><path d="M765 543H675L548 432"/>
</g>
<g class="diagram-copy">
<text x="44" y="156" class="diagram-label">{label('guide_prev')}</text><text x="44" y="181" class="diagram-detail">{label('guide_key_up')}</text>
<text x="710" y="178" class="diagram-label">{label('guide_next')}</text><text x="710" y="203" class="diagram-detail">{label('guide_key_down')}</text>
<text x="715" y="65" class="diagram-label">{label('guide_power_detail')}</text><text x="715" y="89" class="diagram-detail">{label('guide_power')}</text>
<text x="44" y="496" class="diagram-label">BACK</text><text x="44" y="520" class="diagram-detail">{label('guide_back')}</text>
<text x="258" y="533" class="diagram-label">OK</text><text x="258" y="557" class="diagram-detail">{label('guide_ok')}</text>
<text x="614" y="496" class="diagram-label">→</text><text x="614" y="520" class="diagram-detail">{label('guide_next')}</text>
<text x="776" y="533" class="diagram-label">←</text><text x="776" y="557" class="diagram-detail">{label('guide_prev')}</text>
</g></svg></div></section>'''


def render_page(language: str, page: str) -> bytes:
    t = COPY[language]
    if page == "home":
        body = f'''<section class="home-hero"><div class="hero-copy"><p class="product-type">PagePet Reader · Xteink X3</p><h1>{escape(t['home_title'])}</h1><p class="lead">{escape(t['home_intro'])}</p><div class="actions"><a class="button" href="{_link(language, 'downloads')}">{escape(t['home_action'])}<span aria-hidden="true">↗</span></a><a class="secondary-link" href="{_link(language, 'convert')}">{escape(t['home_secondary'])}</a><a class="secondary-link" href="{_link(language, 'guide')}">{escape(t['home_guide'])}</a></div><p class="build-status">{escape(t['home_status'])}</p></div><div class="dragon-panel"><img src="/dragon.png" alt="{'Green pixel dragon reading a book' if language == 'en' else 'Зелёный пиксельный дракончик читает книгу'}" width="1254" height="1254"></div></section>
<section class="features"><h2>{escape(t['feature_title'])}</h2><div class="feature-grid">{''.join(f'<article><span class="pixel-icon" aria-hidden="true">{icon}</span><h3>{escape(t[f"feature_{n}_title"])}</h3><p>{escape(t[f"feature_{n}"])}</p></article>' for n, icon in ((1, '▤'), (2, '✦'), (3, '↗')))}</div></section>'''
    elif page == "downloads":
        body = f'''<section class="page-intro"><p class="product-type">PagePet Reader · Xteink X3</p><h1>{escape(t['downloads_title'])}</h1><p class="lead">{escape(t['downloads_intro'])}</p></section>
<section class="download-section"><div class="notice"><span class="status-dot" aria-hidden="true"></span><div><h2>{escape(t['downloads_notice_title'])}</h2><p>{escape(t['downloads_notice'])}</p></div></div><div class="device-grid">{''.join(f'<article class="device-card"><div class="device-glyph" aria-hidden="true">▣</div><h3>{escape(t[name])}</h3><span>{escape(t["device_status"])}</span></article>' for name in ('device_x3',))}</div><div class="download-links"><a class="button" href="https://t.me/pagepet_reader">{escape(t['downloads_follow'])}<span aria-hidden="true">↗</span></a><a class="secondary-link" href="https://github.com/7box-studio/pagepet-reader">{escape(t['downloads_source'])}</a></div></section>
<section class="information"><h2>{escape(t['downloads_next_title'])}</h2><p>{escape(t['downloads_next'])}</p></section>'''
    elif page == "convert":
        body = f'''<section class="page-intro"><p class="product-type">TXT · EPUB · FB2</p><h1>{escape(t['convert_title'])}</h1><p class="lead">{escape(t['convert_intro'])}</p></section><section class="convert-layout"><form class="converter-card" id="convert-form" data-language="{language}" data-missing="{escape(t['convert_missing'])}" data-invalid="{escape(t['convert_invalid'])}" data-same="{escape(t['convert_same'])}" data-working="{escape(t['convert_working'])}" data-success="{escape(t['convert_success'])}" data-failed="{escape(t['convert_failed'])}" data-button="{escape(t['convert_button'])}" data-select="{escape(t['select_file'])}"><label class="drop-zone" id="drop-zone" for="book-file"><span class="upload-icon" aria-hidden="true">↥</span><strong id="file-label">{escape(t['select_file'])}</strong><span>{escape(t['drop_file'])}</span></label><input id="book-file" name="file" type="file" accept=".epub,.fb2,.mobi,.azw3,.docx,.txt,.rtf,.odt" required><p class="limit">{escape(t['limit'])}</p><div class="format-row"><label for="output-format">{escape(t['output_label'])}</label><select id="output-format" name="format">{''.join(f'<option value="{format_name}">{format_name.upper()}</option>' for format_name in ('txt', 'epub', 'fb2', 'mobi', 'azw3', 'docx'))}</select></div><button class="button convert-button" type="submit">{escape(t['convert_button'])}<span aria-hidden="true">↗</span></button><p id="status" class="status" role="status" aria-live="polite">{escape(t['convert_idle'])}</p></form><aside class="convert-help"><div class="device-glyph" aria-hidden="true">▣</div><h2>{escape(t['convert_usage_title'])}</h2><p>{escape(t['convert_usage'])}</p></aside></section>'''
    elif page == "guide":
        steps = "".join(f'<li><span class="guide-number">{number:02d}</span><div><h2>{escape(t[f"guide_step_{number}_title"])}</h2><p>{escape(t[f"guide_step_{number}"])}</p></div></li>' for number in range(1, 5))
        body = f'''<section class="page-intro guide-intro"><p class="product-type">PagePet Reader · Xteink X3</p><h1>{escape(t['guide_title'])}</h1><p class="lead">{escape(t['guide_intro'])}</p><p class="build-status">{escape(t['guide_status'])}</p></section>
{_device_diagram(t)}
<section class="guide-layout"><ol class="guide-steps">{steps}</ol><aside class="guide-aside"><div class="guide-help"><h2>{escape(t['guide_note_title'])}</h2><p>{escape(t['guide_note'])}</p><a class="secondary-link" href="{_link(language, 'convert')}">{escape(t['guide_convert'])} ↗</a></div></aside></section>'''
    else:
        raise ValueError("Unknown page")
    return _layout(language, page, body)
