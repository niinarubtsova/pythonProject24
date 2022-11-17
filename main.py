from flask import Flask, render_template, request
import utils
from api.api import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp)

@app.route("/")
def view_posts():
    posts = utils.load_posts()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:pk>")
def view_post(pk):
    post = utils.load_post(pk)
    comments = utils.load_comments(pk)
    return render_template("post.html", post=post, comments=comments)


@app.route("/user/<user_name>")
def search_post_by_user_name(user_name):
    posts = utils.user_posts(user_name=user_name)
    return render_template("search.html", posts=posts)


@app.route("/search/")
def search_post():
    word = request.args.get('s', '').lower()
    posts = utils.load_posts(search_word=word)
    return render_template("search.html", posts=posts)


@app.errorhandler(500)
def server_error(e):
    return "500 не волнуйся"


@app.errorhandler(404)
def not_found(e):
    return "404 не волнуйся"




if __name__ == '__main__':
    app.run(debug=True)
