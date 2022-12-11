import grpc

import app.app_pb2
import app.app_pb2_grpc
from app.service.utils import from_pb2_response_to_tuple


class Client:

    def __init__(self):
        self._host = "localhost:50051"
        self._login = None
        self._password = None

    def login(self, login: str, password: str):
        with grpc.insecure_channel(self._host) as channel:
            stub = app.app_pb2_grpc.AuthServiceStub(channel)
            response = stub.Auth(app.app_pb2.AuthData(login=login, password=password))
            response_t = from_pb2_response_to_tuple(response)
            if response_t[0]:
                self._login = login
                self._password = password
        return response_t

    def register(self, nickname: str, login: str, password: str):
        with grpc.insecure_channel(self._host) as channel:
            stub = app.app_pb2_grpc.AuthServiceStub(channel)
            response = stub.Register(app.app_pb2.RegistrationData(nickname=nickname, login=login, password=password))
            return from_pb2_response_to_tuple(response)

    def logout(self):
        with grpc.insecure_channel(self._host) as channel:
            stub = app.app_pb2_grpc.AuthServiceStub(channel)
            response = stub.Logout(app.app_pb2.LogoutData(login=self._login, password=self._password))
            response_t = from_pb2_response_to_tuple(response)
            if response_t[0]:
                self._login = None
                self._password = None
        return response_t

    def change_nickname(self, new_nickname: str):
        with grpc.insecure_channel(self._host) as channel:
            stub = app.app_pb2_grpc.AuthServiceStub(channel)
            response = stub.ChangeNickname(app.app_pb2.NewNicknameData(new_nickname=new_nickname, login=self._login, password=self._password))
        return from_pb2_response_to_tuple(response)


def run():
    client = Client()
    print("register - регистрация в системе\nlogin - вход в систему\nlogout - выход из системы\nchange - изменить никнейм\nexit - завершить сеанс")
    while True:
        cmd = input("> ")
        if cmd == "register":
            nickname = input("nickname: ")
            login = input("login: ")
            password = input("password: ")
            if nickname and login and password:
                response = client.register(nickname, login, password)
                print(response[3])
            else:
                print("Некорректные данные")
        elif cmd == "login":
            login = input("login: ")
            password = input("password: ")
            if login and password:
                response = client.login(login, password)
                print(response[3])
                if response[0]:
                    print(f"Привет, {response[1]}!")
            else:
                print("Некорректные данные")
        elif cmd == "logout":
            response = client.logout()
            print(response[3])
        elif cmd == "change":
            new_nickname = input("new_nickname: ")
            if new_nickname:
                response = client.change_nickname(new_nickname)
                print(response[3])
                if response[0]:
                    print(f"Новый никнейм: {response[1]}")
            else:
                print("Некорректные данные")
        elif cmd == "exit":
            break


if __name__ == "__main__":
    run()
