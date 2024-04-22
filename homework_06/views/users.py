import logging

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import DatabaseError, IntegrityError
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

from models.database import db
from models.user import User

users_app = Blueprint("users_app", __name__)


@users_app.route("/", endpoint="list")
def list_users():
    users = User.query.order_by(User.id).all()
    return render_template(
        "users/list.html",
        users=users,
    )


def get_username_from_form():
    username = request.form.get("username")
    if name := (username and username.strip()):
        return name

    raise BadRequest("field username is required!")


def get_name_from_form():
    user_name = request.form.get("name")
    if name := (user_name and user_name.strip()):
        return name

    raise BadRequest("field name is required!")


def get_email_from_form():
    email = request.form.get("email")
    if name := (email and email.strip()):
        return name

    raise BadRequest("field email is required!")


def save_user(name):
    try:
        db.session.commit()
    except IntegrityError as ex:
        logging.warning("got integrity error with text %s", ex)
        raise BadRequest(f"Could not save user {name}, probably username is not unique")
    except DatabaseError:
        db.session.rollback()
        logging.exception("got db error!")
        raise InternalServerError(f"could not save user with name {name}!")


@users_app.route("/<int:user_id>/", methods=["GET"], endpoint="details")
def get_user_by_id(user_id: int):
    user = User.query.get(user_id)
    if user is None:
        raise NotFound(f"User with id #{user_id} not found!")

    return render_template(
            "users/details.html",
            user=user
        )


@users_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_user():
    if request.method == "GET":
        return render_template("users/add.html")

    name = get_name_from_form()
    username = get_username_from_form()
    email = get_email_from_form()
    user = User(name, username, email)
    db.session.add(user)
    save_user(user.name)
    return redirect(url_for("users_app.details", user_id=user.id))
