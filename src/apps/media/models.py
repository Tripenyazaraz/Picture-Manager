from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.fields import SET_NULL
from tortoise.models import Model
from tortoise import fields


class Media(Model):
    id = fields.IntField(pk=True)
    filename = fields.CharField(max_length=254)
    filepath = fields.CharField(max_length=2032)
    uploaded_by = fields.ForeignKeyField('user.User', on_delete=SET_NULL, null=True)
    tags = fields.ManyToManyField('tag.Tag')


Media_Pydantic = pydantic_model_creator(Media, name="Media")
