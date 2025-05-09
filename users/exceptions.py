from fastapi import status, HTTPException


class UserNotFound(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = 'User not found'


class InvalidEmail(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_406_NOT_ACCEPTABLE
        self.detail = 'Email already in use'


class IncorrectAccessData(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = 'Incorrect access data'


class AuthenticationUnauthorized(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = 'Unable to authenticate_user credential'
        self.headers = {'WWW-Authenticate': 'Bearer'}
