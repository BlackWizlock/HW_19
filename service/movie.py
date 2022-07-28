from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, movid):
        return self.dao.get_one(movid)

    def get_all(self, filters):
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, movid):
        return self.dao.create(movid)

    def update(self, movid):
        self.dao.update(movid)
        return self.dao

    def delete(self, movid):
        self.dao.delete(movid)
