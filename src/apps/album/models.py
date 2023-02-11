from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.fields import SET_NULL
from tortoise.models import Model
from tortoise import fields


class Album(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=254)
    created_by = fields.ForeignKeyField('user.User', on_delete=SET_NULL, null=True)
    medias = fields.ManyToManyField('media.Media')


Album_Pydantic = pydantic_model_creator(Album, name="Album")

