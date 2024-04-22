import os

from flask import Flask, render_template
from flask_migrate import Migrate

from models.database import db
from views.users import users_app
from views.posts import posts_app

app = Flask(__name__)
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(posts_app, url_prefix="/posts")

#app.config.update(
#    SQLALCHEMY_TRACK_MODIFICATIONS=False,
#    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
#)

CONFIG_OBJ_PATH = "config.{}".format(os.getenv("CONFIG", "DevelopmentConfig"))
app.config.from_object(CONFIG_OBJ_PATH)

db.init_app(app)

migrate = Migrate(app, db)


@app.route("/", endpoint="home")
def root():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
