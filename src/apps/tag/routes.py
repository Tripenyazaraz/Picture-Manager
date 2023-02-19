from fastapi import APIRouter

from src.apps.tag.views import TagView
from src.base.routes import ViewSetRouter

router = APIRouter()

router.include_router(ViewSetRouter(
    prefix="tag",
    view=TagView,
    response_model=None,
    tags=["Tag"])
)
