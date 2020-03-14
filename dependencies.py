from injector import singleton
from services.db import Database
from api.movie_api import MovieAPI
from services.movie_service import MovieService


def configure(binder):
    binder.bind(Database, to=Database, scope=singleton)
    binder.bind(MovieService, to=MovieService, scope=singleton)
    binder.bind(MovieAPI, to=MovieAPI, scope=singleton)