import bcrypt

from survey.extensions import db

from .base import Base


class Survey(Base):
    __tablename__ = "survey"

    title = db.Column(db.String(length=64))
    description = db.Column(db.String(length=256))
    active_till = db.Column(db.DateTime())
    active_from = db.Column(db.DateTime())
    questions = db.relationship("Question", backref="survey", cascade="all, delete, delete-orphan")