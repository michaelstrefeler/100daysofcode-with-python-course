#!python3

from flask import Flask, render_template
from data import upcoming_games

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html",
                           upcoming_games=upcoming_games)


if __name__ == "__main__":
    app.run()
