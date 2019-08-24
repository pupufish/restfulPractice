from common.ma import ma
from marshmallow import validate
from modules.user import UserModel
#from modules.schema.post import PostSchema


class UserSchema(ma.Schema):
    class Meta:
        model = UserModel

    id = ma.Int()
    name = ma.Str()
    email = ma.Email(required=True)
    password = ma.Str(required=True, validate=[validate.Length(min=6, max=36)])
    #post = ma.List(ma.Nested(PostSchema))
