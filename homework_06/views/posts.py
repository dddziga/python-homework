import logging

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import DatabaseError, IntegrityError
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

from models.post import Post
from models.database import db

posts_app = Blueprint("posts_app", __name__)
users_app = Blueprint("users_app", __name__)


@posts_app.route("/", endpoint="list")
def list_posts():
    posts = Post.query.order_by(Post.id).all()
    return render_template(
        "posts/list.html", posts=posts
    )


def save_post(title):
    try:
        db.session.commit()
    except IntegrityError as ex:
        logging.warning("got integrity error with text %s", ex)
        raise BadRequest(f"Could not save post {title}, probably name is not unique")
    except DatabaseError:
        db.session.rollback()
        logging.exception("got db error!")
        raise InternalServerError(f"could not save post with name {title}!")


@posts_app.route("/<int:post_id>/", methods=["GET", "POST"], endpoint="details")
def get_post_by_id(post_id: int):
    post = Post.query.get(post_id)
    if post is None:
        raise NotFound(f"Post with id #{post_id} not found!")

    return render_template(
            "posts/details.html",
            post=post
        )


def get_title_from_form():
    title = request.form.get("title")
    if name := (title and title.strip()):
        return name

    raise BadRequest("field title is required!")


def get_body_from_form():
    body = request.form.get("content")
    if content := (body and body.strip()):
        return content

    raise BadRequest("field content is required!")


def get_user_id_post_from_form():
    user = request.form.get("user_id")
    if user_id := (user and user.strip()):
        return user_id

    raise BadRequest("field user is required!")


@posts_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_post():
    if request.method == "GET":
        return render_template("posts/add.html")

    title = get_title_from_form()
    body = get_body_from_form()
    user_id = get_user_id_post_from_form()
    post = Post(user_id, title, body)
    db.session.add(post)
    save_post(post.title)
    return redirect(url_for("posts_app.details", post_id=post.id))
