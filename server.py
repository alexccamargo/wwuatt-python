import datetime
import logging
import os

from flask import Flask, jsonify

from services.movie_service import MovieService
from services.db import Database


app = Flask(__name__)

logger = logging.getLogger()

@app.route("/", methods=["GET"])
def index():
    database = Database()
    movie_service = MovieService(database)

    return jsonify(movie_service.allMovies())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
