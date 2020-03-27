# endpoints.py
from flask import Blueprint, jsonify
from flask_restful import Resource, Api

from models import *
from schema import *

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

platform_schema = PlatformSchema()
platforms_schema = PlatformSchema(many=True)

status_schema = StatusSchema()
statuses_schema = StatusSchema(many=True)


@api_bp.route('/')
def health():
    return jsonify({"message": "it's alive!"})


class GenreRes(Resource):
    def get(self):
        genres = Genre.query.all()
        return jsonify(genres_schema.dump(genres))


class PlatformRes(Resource):
    def get(self):
        platforms = Platform.query.all()
        return jsonify(platforms_schema.dump(platforms))


class StatusRes(Resource):
    def get(self):
        statuses = Status.query.all()
        return jsonify(statuses_schema.dump(statuses))

api.add_resource(GenreRes, '/genre')
api.add_resource(PlatformRes, '/platform')
api.add_resource(StatusRes, '/status')
