from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Degim",
        "umur": 20,
        "NRP": "05311940000042"
    },
    {
        "name": "Didude",
        "umur": 19,
        "NRP": "05311940000019"
    },
    {
        "name": "Paael",
        "umur": 20,
        "NRP": "05311940000025"
    }
]

class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("umur")
        parser.add_argument("NRP")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "umur": args["umur"],
            "NRP": args["NRP"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("umur")
        parser.add_argument("NRP")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["umur"] = args["umur"]
                user["NRP"] = args["NRP"]
                return user, 200

        user = {
            "name": name,
            "umur": args["umur"],
            "NRP": args["NRP"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

api.add_resource(User, "/user/<string:name>")

app.run(debug=True)
