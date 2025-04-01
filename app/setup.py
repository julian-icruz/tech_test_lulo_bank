from fastapi import FastAPI
from fastapi.routing import APIRouter
from fastapi.middleware.cors import CORSMiddleware

from app.container import AppContainer

from app.extract.routes import router as extract_router
from app.transform.routes import router as transform_router
from app.load.routes import router as load_router


APP_TITLE = "Api technical test for Lulo Bank"
APP_DESCRIPTION = (
    "This is the api technical test for Lulo Bank to see the documentation go to /docs"
)
APP_VERSION = "0.0.1"
APP_TERMS_OF_SERVICE = "http://example.com/terms/"
APP_CONTACT = {
    "name": "API Support",
    "url": "http://www.example.com/support",
    "email": "julian.iguavita@outlook.com",
}


def _create_app() -> FastAPI:
    app = FastAPI(
        title=APP_TITLE,
        description=APP_DESCRIPTION,
        version=APP_VERSION,
        terms_of_service=APP_TERMS_OF_SERVICE,
        contact=APP_CONTACT,
    )
    add_middleware(app)
    app.container = _build_application_container()
    app.include_router(_build_v1_router())
    return app


def add_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


def _build_application_container():
    container = AppContainer()
    container.init_resources()
    return container


def _build_v1_router():
    router = APIRouter(prefix="/v1")
    router.include_router(extract_router)
    router.include_router(transform_router)
    router.include_router(load_router)
    return router
