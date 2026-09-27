# PagePet services plan

This document describes the public services around PagePet Reader. It belongs to the landing repository so the site, bot, and conversion workflow can evolve separately from the firmware.

## Repository boundaries

- `pagepet-landing` owns the one-page site, product explanation, screenshots, supported-device list, release links, installation and recovery guidance, and links to the PagePet Reader and 7box-studio channels.
- `pagepet-converter-core` is the shared conversion repository. It contains the format conversion library and a local command-line interface, plus format tests. It has no Telegram or web code, network access, credentials, or user interface.
- `pagepet-bot` owns the Telegram conversation: receiving a book, showing the available conversion choices, sending progress and error messages, and returning the result. It includes `pagepet-converter-core` as a submodule at a reviewed commit.
- `pagepet-landing` owns the public site. If a web upload form is added, its backend or worker includes the same `pagepet-converter-core` submodule and exposes a small versioned endpoint to the browser. The browser does not carry a second conversion implementation.

The landing page, Telegram bot, and converter core are separate repositories. The core is intentionally a submodule of the bot and the site's server-side conversion component. It is not a submodule of the firmware. The firmware repository should stay focused on the device and must not receive server dependencies or bot tokens.

## First useful version

1. Publish a calm explanation of PagePet Reader as a CrossPoint Reader based firmware fork with an optional reading companion.
2. Add a short supported-device and installation section only after the corresponding firmware build and device test exist.
3. Create `pagepet-converter-core` and build a local command with one tested input/output path before adding Telegram or web code.
4. Add the core as a submodule to `pagepet-bot` and verify that the bot handles size limits, errors, retries, and temporary-file deletion around the conversion call.
5. Add the same core submodule to the site's backend or worker only when a web upload is needed. Keep an explicit endpoint version and repeat the cleanup and limit checks there.
6. Start with a small list of formats and expand it only when real files are tested on PagePet Reader.

## Questions to settle before launch

- Which input formats are needed most often, and which output format is the most reliable for PagePet Reader?
- What maximum file size and request rate can the service handle safely?
- How long, if at all, should temporary files exist during conversion?
- What should the bot say when a file is unsupported, damaged, too large, or conversion fails?
- Which endpoint and API version should the landing page expose if browser upload is added?

Do not publish a bot token, deployment secret, user-uploaded book, or private infrastructure setting in this repository.
