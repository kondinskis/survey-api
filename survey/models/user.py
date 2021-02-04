from survey.extensions import db

from .base import Base


class User(Base):
    __tablename__ = "user"

    firstname = db.Column(db.String(length=32))
    lastname = db.Column(db.String(length=32))
    email = db.Column(db.String(length=64), nullable=False)
    password_hash = db.Column(db.String(length=128), nullable=False)

    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    role = db.relationship("Role")