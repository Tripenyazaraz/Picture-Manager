from src.apps.media.models import Media_Pydantic, Media
from src.core.mixins import ModelViewSet


class MediaView(ModelViewSet):
    model = Media
    pydantic_model = Media_Pydantic
