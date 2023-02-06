from tortoise.fields import SET_NULL
from tortoise.models import Model
from tortoise import fields


class MediaModel(Model):
    id = fields.IntField(pk=True)
    filename = fields.CharField(max_length=254)
    filepath = fields.CharField(max_length=2032)
    uploaded_by = fields.ForeignKeyField('user.UserModel', on_delete=SET_NULL, null=True)
    tags = fields.ManyToManyField('tag.TagModel')
