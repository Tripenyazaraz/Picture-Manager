from tortoise.models import Model
from tortoise import fields


class UserModel(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=32)
    password = fields.CharField(max_length=64)
    email = fields.CharField(max_length=254)
