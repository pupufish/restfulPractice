from flask import Flask
from flask_restful import Api

from resources.user import User, Users

app = Flask(__name__)
api = Api(app)

api.add_resource(User, "/user/<string:name>")  # <a:b> no blank
api.add_resource(Users, "/users/")

if __name__ == "__main__":
    from common.ma import ma
    ma.init_app(app)
    app.run()
