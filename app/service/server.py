from concurrent import futures

import grpc

import app.app_pb2
import app.app_pb2_grpc
from app.service.db import RegisteredUsersDB
from app.service.utils import to_pb2, get_md5


class Server(app.app_pb2_grpc.AuthServiceServicer):

    def __init__(self):
        self._db = RegisteredUsersDB()
        self._active_users = set()

    def Register(self, request, context):
        success = True
        if not self._db.exists_login(request.login):
            if not self._db.exists_nickname(request.nickname):
                password = get_md5(request.password)
                self._db.register(
                    request.nickname,
                    request.login,
                    password
                )
                # self._active_users.add((request.login, password))
                info = "Регистрация прошла успешно"
            else:
                success = False
                info = "Пользователь с данным никнеймом уже существует"
        else:
            success = False
            info = "Пользователь с данным логином уже существует"
        return to_pb2(success, request.nickname, request.login, info)

    def Auth(self, request, context):
        success = True
        password = get_md5(request.password)
        user = self._db.get(request.login, password)
        if user:
            self._active_users.add((request.login, password))
            info = "Вход выполнен успешно"
        else:
            success = False
            info = "Пользователь с такими данными не существует"
        return to_pb2(success, request.login, user["nickname"] if user else None, info)

    def ChangeNickname(self, request, context):
        success = True
        new_nickname = request.new_nickname
        login = request.login
        password = get_md5(request.password)
        if (login, password) in self._active_users:
            if not self._db.exists_nickname(new_nickname):
                user = self._db.get(login, password)
                user["nickname"] = new_nickname
                info = "Никнейм был успешно изменен"
            else:
                success = False
                info = "Пользователь с таким никнеймом уже существует"
        else:
            success = False
            info = "Необходимо выполнить выход"
        return to_pb2(success, login, new_nickname, info)

    def Logout(self, request, context):
        success = True
        login = request.login
        password = get_md5(request.password)
        if (login, password) in self._active_users:
            self._active_users.remove((login, password))
            info = "Успешный выход из системы"
        else:
            success = False
            info = "Необходимо выполнить выход"
        return to_pb2(success, None, login, info)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    app.app_pb2_grpc.add_AuthServiceServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Server stopped by keyboard interrupt")


if __name__ == "__main__":
    serve()
