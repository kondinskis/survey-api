from flask_restx import fields
from survey.namespaces.survey import ns

schema = ns.model(
    "Survey schema",
    {},
)