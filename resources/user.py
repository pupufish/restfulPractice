from flask_restful import Resource
from modules.schema.user import UserSchema
from flask import request
from modules.user import UserModel

user_schema = UserSchema(many=False)


def get_param():
    data = request.get_json(force=False)
    if data is None:
        data = request.form
    return data


class User(Resource):

    def get(self, name):
        user = UserModel.get_user(name)
        if not user:
            return {'State': 'Failed', 'msg': "Username is not exit"}, 403
        return {
            'State': 'Success',
            'msg': "show the user %s" % name,
            'user': user_schema.dump(user)
        }

    def post(self, name):
        data = get_param()
        result = user_schema.load(data)
        user = UserModel(name, result['email'], result['password'])
        user.add_user()
        return {
            'State': 'Success',
            'msg': "Insert user to users",
            'user': user_schema.dump(user)
        }

    # not work
    def put(self, name):
        result = user_schema.load(get_param())
        user = UserModel.get_user(name)
        if not user:
            return {'State': 'Failed', 'msg': "User not exist"}, 403
        user.email = result['email']
        user.password = result['password']

        return {
            'State': 'Success',
            'msg': "update %s" % name,
            'user': user_schema.dump(user)
        }

    def delete(self, name):
        UserModel.delete_user(name)
        return {'State': 'Success', 'msg': 'Delete complete'}


class Users(Resource):
    def get(self):
        return {
            'msg': "Get all users",
            'users': user_schema.dump(UserModel.get_all_user(), many=True)
        }
