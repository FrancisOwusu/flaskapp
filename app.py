"""app module"""

from flask import Flask,make_response
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    """_summary_

    Returns:
        _type_: _description_
    """
    res = make_response("<b> My first Flask application in action! </b>")
    res.status_code = 200
    return res
  #  return "<p>Hello, World!</p>"


@app.route("/<name>")
def get_name(name):
    """Get user name from route"""
    return f"Hello,my name is {escape(name)}!"


@app.route("/user/<username>")
def show_user_profile(username):
    """username"""
    # show the user profile for that user
    return f"User {escape(username)}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    """post_id"""
    # show the post with the given id, the id is an integer
    return f"Post {post_id}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    """subpath"""
    # show the subpath after /path/
    return f"Subpath {escape(subpath)}"


@app.route("/projects/")
def projects():
    """projects"""
    return "The project page"


@app.route("/about")
def about():
    """about"""
    return "The about page"
