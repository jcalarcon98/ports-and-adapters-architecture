from fastapi import APIRouter, FastAPI

from .api_version import APIVersion


class RouterVersionManager:
    def __init__(self, app: FastAPI, version: APIVersion):
        self.app = app
        self.version = version

    def register_router(self, router: APIRouter):
        self.app.include_router(router, prefix=f'/api/{self.version.value}')
