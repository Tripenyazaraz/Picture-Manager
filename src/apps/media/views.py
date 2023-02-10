from src.apps.media.models import Media_Pydantic, MediaModel
from src.core.mixins import ModelViewSet


class MediaView(ModelViewSet):
    model = MediaModel
    pydantic_model = Media_Pydantic
