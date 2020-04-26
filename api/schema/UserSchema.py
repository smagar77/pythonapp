from marshmallow import fields
from api import ma
from api.models.Users.UserModel import UserModel

class UserSchema(ma.ModelSchema):
    '''UserSchema class handle users schema'''
    class Meta:
        model = UserModel

    id = fields.Integer()
    username = fields.String()
    password = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()
    created_on = fields.DateTime()
    last_login = fields.DateTime()

user_schema = UserSchema()