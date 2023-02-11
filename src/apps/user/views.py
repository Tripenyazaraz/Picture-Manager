from src.apps.user.models import User, User_Pydantic
from src.core.mixins import ModelViewSet


class UserView(ModelViewSet):
    model = User
    pydantic_model = User_Pydantic
