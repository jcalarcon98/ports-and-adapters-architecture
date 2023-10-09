import typing

from fastapi import APIRouter

version_router = APIRouter(prefix='/version')


@version_router.get('')
def get_version() -> typing.Dict[str, str]:
    return {"Ports and Adapter Architecture": "v0.0.1"}
