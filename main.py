from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

names = {
    "tamim": {
        "age": 27,
        "occupation": "student"
    },
    "Ida": {
        "age": 25,
        "occupation": "student"
    }
}

hello_post_args = reqparse.RequestParser()
hello_post_args.add_argument("name", type=str, required=True, help="Name cannot be blank")
hello_post_args.add_argument("views", type=str, required=True, help="views cannot be blank")
hello_post_args.add_argument("likes", type=str, required=True, help="likes cannot be blank")


class HelloWorld(Resource):

    def get(self, name):
        return names[name]

    def post(self, name):
        args = hello_post_args.parse_args()
        return {
            "name": args["name"],
            "views": args["views"],
            "likes": args["likes"]
        }


api.add_resource(HelloWorld, '/helloworld/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
