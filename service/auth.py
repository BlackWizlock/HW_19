import calendar
import datetime

import jwt

from config import Config
from service.user import UserService


class AuthService:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def generate_token(self, username: str, password: str, is_refresh: bool = False) -> None or dict:
        user = self.user_service.get_by_name(username)

        if user is None:
            return '', 400

        if not is_refresh:
            if not self.user_service.compare_password(user.password, password):
                return '', 401

        data = {
                'username': user.username,
                'role'    : user.role
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, Config.SECRET_HERE, algorithm=Config.ALGORITH)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, Config.SECRET_HERE, algorithm=Config.ALGORITH)

        return {
                'access_token' : access_token,
                'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token: str):
        data = jwt.decode(jwt=refresh_token, key=Config.SECRET_HERE, algorithms=[Config.ALGORITH])
        username = data.get('username')

        return self.generate_token(username, None, is_refresh=True)
