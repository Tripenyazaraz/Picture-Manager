from fastapi import APIRouter

from src.apps.media.views import MediaView
from src.core.routes import ViewSetRouter

router = APIRouter()

router.include_router(ViewSetRouter(
    prefix="media",
    view=MediaView,
    response_model=None,
    tags=["Media"])
)
