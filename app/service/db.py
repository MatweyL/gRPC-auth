import json
import os.path


class RegisteredUsersDB:

    def __init__(self):
        self._registered_users = []
        self._load_registered_users()

    def get(self, login, password):
        for registered_user in self._registered_users:
            if registered_user["login"] == login and registered_user["password"] == password:
                return registered_user

    def register(self, nickname, login, password):
        self._registered_users.append(
            {"nickname": nickname, "login": login, "password": password}
        )
        self._save_registered_users()

    def change_nickname(self, new_nickname, login):
        for registered_user in self._registered_users:
            if registered_user["login"] == login:
                registered_user["nickname"] = new_nickname
                return registered_user

    def exists_nickname(self, nickname):
        for registered_user in self._registered_users:
            if registered_user["nickname"] == nickname:
                return True
        return False

    def exists_login(self, login):
        for registered_user in self._registered_users:
            if registered_user["login"] == login:
                return True
        return False

    def _load_registered_users(self):
        if os.path.exists("registered_users.json"):
            with open("registered_users.json") as json_file:
                self._registered_users = json.load(json_file)

    def _save_registered_users(self):
        with open("registered_users.json", "w") as json_file:
            json.dump(self._registered_users, json_file)
