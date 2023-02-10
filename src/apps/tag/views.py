from src.apps.tag.models import TagModel, Tag_Pydantic
from src.core.mixins import ModelViewSet


class TagView(ModelViewSet):
    model = TagModel
    pydantic_model = Tag_Pydantic
