from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from tortoise import fields


class TagModel(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64)
    type = fields.CharField(max_length=64)


Tag_Pydantic = pydantic_model_creator(TagModel, name="Tag")
