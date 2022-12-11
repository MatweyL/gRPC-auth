from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AuthData(_message.Message):
    __slots__ = ["login", "password"]
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    login: str
    password: str
    def __init__(self, login: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LogoutData(_message.Message):
    __slots__ = ["login", "password"]
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    login: str
    password: str
    def __init__(self, login: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class NewNicknameData(_message.Message):
    __slots__ = ["login", "new_nickname", "password"]
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    NEW_NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    login: str
    new_nickname: str
    password: str
    def __init__(self, new_nickname: _Optional[str] = ..., login: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class RegistrationData(_message.Message):
    __slots__ = ["login", "nickname", "password"]
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    login: str
    nickname: str
    password: str
    def __init__(self, nickname: _Optional[str] = ..., login: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class ResponseData(_message.Message):
    __slots__ = ["info", "login", "nickname", "success"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    info: str
    login: str
    nickname: str
    success: bool
    def __init__(self, success: bool = ..., nickname: _Optional[str] = ..., login: _Optional[str] = ..., info: _Optional[str] = ...) -> None: ...
