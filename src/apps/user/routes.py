from fastapi import APIRouter

from src.apps.user.views import UserView
from src.base.routes import ViewSetRouter

router = APIRouter()

router.include_router(ViewSetRouter(
    prefix="user",
    view=UserView,
    response_model=None,
    tags=["User"])
)
