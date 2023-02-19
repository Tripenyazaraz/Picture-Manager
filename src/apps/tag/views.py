from src.apps.tag.models import Tag, Tag_Pydantic
from src.base.mixins import ModelViewSet


class TagView(ModelViewSet):
    model = Tag
    pydantic_model = Tag_Pydantic
