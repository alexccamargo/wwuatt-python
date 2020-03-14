
class MovieService:
    def __init__(self, database):
        self.database = database
    
    def allMovies(self):
        movies = []
        with self.database.db.connect() as conn:
            # Execute the query and fetch all results
            allMovies = conn.execute(
                "SELECT title FROM movies"
            ).fetchall()
            # Convert the results into a list of dicts representing votes
            for row in allMovies:
                movies.append({"title": row[0]})
        return movies
