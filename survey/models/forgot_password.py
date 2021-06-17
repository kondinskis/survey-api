import bcrypt

from survey.extensions import db

from .base import Base


class ForgotPassword(Base):
    __tablename__ = "forgot_password"

    token = db.Column(db.String(length=64))
    expires_at = db.Column(db.DateTime(timezone=True))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User")
