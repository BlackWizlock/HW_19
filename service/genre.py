from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO) -> None:
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, gid):
        return self.dao.create(gid)

    def update(self, gid):
        self.dao.update(gid)
        return self.dao

    def delete(self, gid):
        self.dao.delete(gid)
