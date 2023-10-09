from fastapi import FastAPI

from .routers import RouterVersionManager, APIVersion
from .routers.v1 import version_router


def create_app() -> FastAPI:
    app = FastAPI()

    v1_routes = RouterVersionManager(app=app, version=APIVersion.V1)
    v1_routes.register_router(version_router)

    return app
