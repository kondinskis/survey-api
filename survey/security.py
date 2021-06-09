'''Security utitlities
'''
from functools import wraps

from flask_jwt_extended import current_user
from werkzeug.exceptions import Unauthorized

class allowed_for:

    def __init__(self, *roles):
        self.roles = roles or []
    
    def __call__(self, method):
        
        @wraps(method)
        def _check_roles_wrapper(*args, **kwargs):
            if not self.user_role_in_allowed_roles():
                raise Unauthorized('Insufficient privileges')
            return method(*args, **kwargs)
        
        return _check_roles_wrapper

    def user_role_in_allowed_roles(self):
        role = current_user.role.name
        return role in self.roles