from enum import Enum

from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from tortoise import fields


class TagTypeEnum(Enum):
    general = 'general'
    author = 'author'
    character = 'character'
    fandom = 'fandom'
    meta = 'meta'


class Tag(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64)
    type = fields.CharEnumField(TagTypeEnum, max_length=64)


Tag_Pydantic = pydantic_model_creator(Tag, name="Tag")
