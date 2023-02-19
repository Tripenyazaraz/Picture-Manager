from fastapi import APIRouter

from src.apps.album.views import AlbumView
from src.base.routes import ViewSetRouter

router = APIRouter()

router.include_router(ViewSetRouter(
    prefix="album",
    view=AlbumView,
    response_model=None,
    tags=["Album"])
)
