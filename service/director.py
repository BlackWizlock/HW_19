from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO) -> None:
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, did):
        return self.dao.create(did)

    def update(self, did):
        self.dao.update(did)
        return self.dao

    def delete(self, did):
        self.dao.delete(did)
