from flask import Flask, render_template, url_for


app = Flask(__name__, instance_relative_config=True)


@app.route("/", methods=["GET"])
def index():
    return "index page"


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello, World"


# Url parameters
@app.route("/user/<username>", methods=["GET"])
def get_user(username: str):
    return f"User({username})"


# Show template page
@app.route("/login", methods=["POST"])
@app.route("/login/<username>", methods=["POST"])
def login(username=None):
    return render_template("login.html", username=username)


# Static files
@app.route("/static/style")
def get_style():
    return url_for("static", filename="style.css")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
