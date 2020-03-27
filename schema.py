# schema.py
from models import *
from backlog import ma


class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genre


class PlatformSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Platform


class StatusSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Status
