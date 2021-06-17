from werkzeug.exceptions import NotFound, BadRequest, Conflict, Forbidden
from datetime import datetime, timezone, timedelta
from secrets import token_urlsafe

from flask_jwt_extended import current_user

from survey.models.user import User
from survey.models.role import Role
from survey.models.forgot_password import ForgotPassword
from survey.extensions import mail
from survey.message_wrap import MessageWrap


class UserService:
    @staticmethod
    def create(user):
        role_id = user.get("role_id")
        role = Role.query.get(role_id)

        password = (user.get("password") or "").strip()
        if not password:
            raise BadRequest("Missing required field: password")

        if role is None:
            raise NotFound(
                description=("Role with id[{0}] not found".format(role_id))
            )

        new_user = User(
            firstname=user.get("firstname", ""),
            lastname=user.get("lastname", ""),
            email=user.get("email"),
            role=role,
        )

        new_user.hash_password(password)

        return new_user.save()

    @staticmethod
    def update(id, user):
        role_id = user.get("role_id")
        role = Role.query.get(role_id)

        if role is None:
            raise NotFound(
                description=("Role with id[{0}] not found".format(role_id))
            )

        saved_user = User.query.get(id)
        if saved_user is None:
            raise NotFound(
                description=("User with id[{0}] not found".format(id))
            )

        saved_user.firstname = user.get("firstname")
        saved_user.lastname = user.get("lastname")
        saved_user.email = user.get("email")
        saved_user.role = role
        saved_user.updated_at = datetime.now(timezone.utc)

        password = user.get("password")
        if not password is None and password.strip():
            saved_user.hash_password(user["password"])

        return saved_user.update()

    @staticmethod
    def delete(id):
        user = User.query.get(id)
        if user is None:
            raise NotFound(
                description=("User with id [{0}] not found".format(id))
            )

        if current_user.id == id:
            raise Conflict(description=("User cannot delete himself"))

        return user.delete()

    @staticmethod
    def get(id):
        user = User.query.get(id)
        if user is None:
            raise NotFound(
                description=("User with id [{0}] not found".format(id))
            )
        return user

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_email(email):
        user = User.query.filter_by(email=email).one_or_none()
        return user

    @staticmethod
    def register(user):
        role = Role.query.filter_by(name="NORMAL").one()

        password = (user.get("password") or "").strip()
        if not password:
            raise BadRequest("Missing required field: password")

        new_user = User(
            firstname=user.get("firstname", ""),
            lastname=user.get("lastname", ""),
            email=user.get("email"),
            role=role,
        )

        new_user.hash_password(user.get("password"))
        new_user.save()

    @staticmethod
    def forgot_password(email):
        user = User.query.filter_by(email=email).one_or_none()

        if user is None:
            return

        ForgotPassword.query.filter_by(user=user).delete()
        forgot_password = ForgotPassword(
            user=user,
            token=token_urlsafe(),
            expires_at=datetime.now(timezone.utc) + timedelta(minutes=5),
        )
        forgot_password.save()

        msg = MessageWrap(
            "Survey Password Reset",
            recipients=[user.email],
            template="forgot_password",
            data={
                "token": forgot_password.token,
            },
        )
        mail.send(msg)

    @staticmethod
    def set_password(token, password):
        forgot_password = ForgotPassword.query.filter_by(
            token=token
        ).one_or_none()

        if forgot_password is None:
            raise NotFound(description=("Token {0} not found".format(token)))

        if forgot_password.expires_at < datetime.now(timezone.utc):
            raise Forbidden(description=("Token {0} expired".format(token)))

        user = forgot_password.user
        user.hash_password(password)
        user.save()

        forgot_password.delete()
