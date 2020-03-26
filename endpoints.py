# endpoints.py
from flask import Blueprint, jsonify

from models import *
from schema import *

api = Blueprint('api', __name__)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

status_schema = StatusSchema()
statuses_schema = StatusSchema(many=True)


@api.route('/')
def health():
    return '{"message": "it\'s alive!"}'


@api.route('/genre', methods=['GET'])
def all_genre():
    genres = Genre.query.all()
    return jsonify(genres_schema.dump(genres))


@api.route('/status', methods=['GET'])
def status():
    statuses = Status.query.all()
    return jsonify(statuses_schema.dump(statuses))
