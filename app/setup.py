from fastapi import FastAPI
from fastapi.routing import APIRouter


APP_TITLE = "Api technical test for Lulo Bank"
APP_DESCRIPTION = "This is the api technical test for Lulo Bank to see the documentation go to /docs"
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
    app.include_router(_build_v1_router())
    return app


def _build_v1_router():
    router = APIRouter(prefix="/v1")
    return router
