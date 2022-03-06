from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_post_args = reqparse.RequestParser()
video_post_args.add_argument("name", type=str, required=True, help="Name cannot be blank")
video_post_args.add_argument("views", type=str, required=True, help="views cannot be blank")
video_post_args.add_argument("likes", type=str, required=True, help="likes cannot be blank")

videos = {}


def abort_if_video_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video {} doesn't exist".format(video_id))

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="Video {} already exists".format(video_id))

class Video(Resource):

    def get(self, video_id):
        abort_if_video_doesnt_exist(video_id)
        return videos[video_id], 200

    def post(self, video_id):
        abort_if_video_exists(video_id)
        args = video_post_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204


api.add_resource(Video, '/videos/<int:video_id>')

if __name__ == '__main__':
    app.run(debug=True)
