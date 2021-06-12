from survey.models.role import Role


class RoleService:
    @staticmethod
    def get_all():
        return Role.query.filter(Role.name!="SYSTEM").all()
