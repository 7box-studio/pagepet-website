from fastapi import FastAPI

from .routes import pages, conversion


def create_app() -> FastAPI:
    app = FastAPI(title="PagePet Website", docs_url=None, redoc_url=None)
    app.include_router(pages.router)
    app.include_router(conversion.router)
    return app
