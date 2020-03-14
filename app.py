import datetime
import logging
import os

from flask import Flask, jsonify
from injector import inject
from dependencies import configure
from flask_injector import FlaskInjector

from api.movie_api import MovieAPI

app = Flask(__name__)

logger = logging.getLogger()

@inject
@app.route("/movies", methods=["GET"])
def movies(api: MovieAPI):
    return jsonify(api.get_movies())

FlaskInjector(app=app, modules=[configure])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
