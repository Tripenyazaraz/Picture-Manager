from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=32)
    password = fields.CharField(max_length=64)
    email = fields.CharField(max_length=254)


User_Pydantic = pydantic_model_creator(User, name="User")
