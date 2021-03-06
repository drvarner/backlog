# models.py
from datetime import datetime
from backlog import db


class Platform(db.Model):
    __tablename__ = 'platform'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Platform {self.name}>'


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Genre {self.name}>'


class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    desc = db.Column(db.String(250))

    def __repr__(self):
        return f'<Status {self.name}>'


class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, index=True)
    added = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    updated = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    purchased = db.Column(db.DateTime)
    completed = db.Column(db.DateTime)

    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    goal_id = db.Column(db.Integer, db.ForeignKey('status.id'))

    def __repr__(self):
        return f'<Game {self.title}>'
