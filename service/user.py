import base64
import hashlib
import hmac

from config import Config
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        return self.dao.create(user_d)

    def update(self, user_d):
        self.dao.update(user_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)

    def make_user_password_hash(self, password: str):
        return base64.b64encode(hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),
                Config.PWD_HASH_SALT,
                Config.PWD_HASH_ITERATIONS
        ))

    def compare_password(self, password_hash, other_password: str) -> bool:
        return hmac.compare_digest(
                base64.b64decode(password_hash),
                hashlib.pbkdf2_hmac(
                        'sha256',
                        other_password.encode('utf-8'),
                        Config.PWD_HASH_SALT,
                        Config.PWD_HASH_ITERATIONS
                ))
