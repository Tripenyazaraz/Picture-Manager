from src.apps.album.models import Album, Album_Pydantic
from src.base.mixins import ModelViewSet


class AlbumView(ModelViewSet):
    model = Album
    pydantic_model = Album_Pydantic
