from src.apps.user.models import UserModel, User_Pydantic
from src.core.mixins import ModelViewSet


class UserView(ModelViewSet):
    model = UserModel
    pydantic_model = User_Pydantic
