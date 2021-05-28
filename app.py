import os
from survey import create_app

app = create_app()


@app.cli.command()
def seed():
    from survey.models.role import Role
    from survey.models.user import User

    roles = [Role(name="SYSTEM"), Role(name="ADMIN"), Role(name="NORMAL")]
    for role in roles:
        role.save()

    role = Role.query.filter_by(name="SYSTEM").one_or_none()

    user = User(firstname="Stefan", lastname="Kondinski", email="kondinskis@gmail.com", role=role)
    user.hash_password("test1234")
    user.save()

if __name__ == "__main__":
    # read host from env, added for Docker to work,
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", debug=True, port=port)
