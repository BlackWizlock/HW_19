import base64
import hashlib
import hmac

from config import Config
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_name(self, name):
        return self.dao.get_by_name(name)

    def create(self, uid):
        uid['password'] = self.make_user_password_hash(uid['password'])
        return self.dao.create(uid)

    def update(self, uid):
        uid['password'] = self.make_user_password_hash(uid['password'])
        self.dao.update(uid)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

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
