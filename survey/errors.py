from sqlalchemy.exc import IntegrityError

from survey.extensions import api


@api.errorhandler(IntegrityError)
def handle_integrity_error(error):
    msg = error.args[0].split("DETAIL:  Key ")[1][:-2]
    return {"message": msg}, 409
