import bcrypt

from survey.extensions import db

from .base import Base


class User(Base):
    __tablename__ = "user"

    firstname = db.Column(db.String(length=32))
    lastname = db.Column(db.String(length=32))
    email = db.Column(db.String(length=64), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=128), nullable=False)

    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    role = db.relationship("Role")

    def hash_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        self.password_hash = hashed_password

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())
