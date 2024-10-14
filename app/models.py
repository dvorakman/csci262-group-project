from flask_login import UserMixin
from flask import current_app

class User(UserMixin):
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password

    @staticmethod
    def get(user_id):
        for user in current_app.users.values():
            if user['id'] == user_id:
                return User(user['id'], user['username'], user['password'])
        return None