
from injector import inject
from services.movie_service import MovieService

class MovieAPI():

    @inject
    def __init__(self, movie_service: MovieService):
        self.movie_service = movie_service

    def get_movies(self):
        return self.movie_service.allMovies()

    