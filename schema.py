# schema.py
from models import Genre, Platform, Status, Criteria, Game
from backlog import ma


class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genre


class StatusSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Status
