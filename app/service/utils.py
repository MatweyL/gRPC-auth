from hashlib import md5


import app.app_pb2


def to_pb2(success, nickname, login, info):
    return app.app_pb2.ResponseData(
        success=success,
        nickname=nickname,
        login=login,
        info=info
    )


def from_pb2_response_to_tuple(response):
    return response.success, response.login, response.nickname, response.info


def get_md5(password):
    return md5(password.encode('utf-8')).hexdigest()
