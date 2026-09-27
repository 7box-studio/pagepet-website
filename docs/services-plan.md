# PagePet services plan

This document describes the public services around PagePet Reader. It belongs to the website repository so the site, bot, and conversion workflow can evolve separately from the firmware.

## Repository boundaries

- `pagepet-website` owns the website, product explanation, supported-device list, release links, installation and recovery guidance, and a browser-based book converter.
- `pagepet-converter-core` is the shared conversion repository. It wraps calibre's `ebook-convert` command and has no Telegram or web code, credentials, or user interface.
- `pagepet-converter-bot` owns the Telegram conversation: receiving a book, showing the available conversion choices, sending progress and error messages, and returning the result. It includes `pagepet-converter-core` as a submodule at a reviewed commit.
- `pagepet-website` owns the public site. If a web upload form is added, its backend or worker includes the same `pagepet-converter-core` submodule and exposes a small versioned endpoint to the browser. The browser does not carry a second conversion implementation.

The website, Telegram bot, and converter core are separate repositories. The website pins the core as a submodule. The firmware repository stays focused on the device and does not receive server dependencies or bot tokens.

## First useful version

1. Publish a calm explanation of PagePet Reader as a CrossPoint Reader based firmware fork with an optional reading companion.
2. Add a short supported-device and installation section only after the corresponding firmware build and device test exist.
3. Use calibre for common book formats through `pagepet-converter-core`, with EPUB as the default output. Exclude PDF.
4. Run the website and converter in Docker. Keep explicit size and concurrency limits, error responses, and temporary-file cleanup.
5. Add the same core as a submodule to `pagepet-converter-bot`. The normal conversation should use buttons, with clear errors and no command typing required. Make an outbound proxy configurable through deployment secrets for environments that need it.
6. Check output formats against real books and PagePet Reader before treating conversion quality as verified. Keep the website independently accessible from Telegram.

## Questions to settle before launch

- What maximum file size and request rate can the service handle safely in production?
- Which converted formats render well on each supported reader?
- What should the bot say when a file is unsupported, damaged, too large, or conversion fails?
- Which endpoint and API version should be used for the bot and website if they share a remote converter service later?

Do not publish a bot token, deployment secret, user-uploaded book, or private infrastructure setting in this repository.
