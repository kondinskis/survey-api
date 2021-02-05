from survey.models.role import Role


class RoleService:
    @staticmethod
    def get_all():
        return Role.query.all()
