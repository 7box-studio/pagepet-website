# PagePet website

Public website for [PagePet Reader](https://github.com/7box-studio/pagepet-reader), a 7box-studio firmware project built on the [FreeInk SDK](https://github.com/Free-Ink/freeink-sdk).

This repository owns the public product explanation: what PagePet Reader is, how the companion works, supported devices, tested releases, installation and recovery instructions, screenshots, and links to the project channels.

The Russian and English reading guides at `/guide` and `/en/guide` describe the current X3 TXT workflow and button controls. They are served by the website and do not add a help screen to the firmware.

Keep both guides and the X3 button diagram in `app/pages.py` synchronized with the firmware's Home, Reading, ReadingSettings, and power-button handlers in `pagepet-reader/src/main.cpp`. Whenever navigation or button behavior changes, update the Russian and English diagram labels, guide steps, and tests in the same change. Physical button positions are based on page 3 of the [official X3 user guide](https://www.xteink.com/pages/user-guide); verify behavior on the device before describing a firmware build as tested. The diagram is an inline SVG on the website, not an on-device asset.

The site is separate from the firmware repository and from the Telegram bot. It must not contain firmware build output, bot credentials, or a second implementation of book conversion.

The initial site plan, including the proposed converter and bot split, is in [docs/services-plan.md](docs/services-plan.md).

The website includes a book converter backed by calibre. It accepts EPUB, FB2, MOBI, AZW3, DOCX, TXT, RTF and ODT, and can produce EPUB, FB2, MOBI, AZW3, DOCX or TXT. For the current Xteink X3 firmware, TXT is the usable on-device format. PDF is intentionally excluded. This is a development preview, not a deployed service or stable firmware download.

Run it locally with Python 3.11+, calibre and the Python dependencies:

```sh
git submodule update --init
python3 -m pip install -r requirements.txt
uvicorn main:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000`. Uploaded files are processed in a temporary directory and removed after each request.

Docker is the intended runtime. For a local container test:

```sh
git submodule update --init
docker compose up --build
```

Open `http://127.0.0.1:8080`. The Compose setup binds only to localhost, runs as a non-root user, and keeps temporary files in a tmpfs. The image has a `/healthz` check. Before public deployment, add a reverse proxy with HTTPS, network rate limits, monitoring, and separate staging/production settings.

Run the website checks after `python3 -m pip install -r requirements-dev.txt` with `python3 -m unittest discover -s tests -v`.
