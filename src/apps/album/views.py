from src.apps.album.models import AlbumModel, Album_Pydantic
from src.core.mixins import ModelViewSet


class AlbumView(ModelViewSet):
    model = AlbumModel
    pydantic_model = Album_Pydantic
