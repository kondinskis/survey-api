import os
from survey import create_app

app = create_app()


@app.cli.command()
def seed():
    from survey.models.role import Role

    roles = [Role(name="SYSTEM"), Role(name="ADMIN"), Role(name="NORMAL")]
    for role in roles:
        role.save()


if __name__ == "__main__":
    # read host from env, added for Docker to work,
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", debug=True, port=port)
