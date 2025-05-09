from fastapi import status, HTTPException


class UserNotFound(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = 'User not found'


class InvalidEmail(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_406_NOT_ACCEPTABLE
        self.detail = 'There is already a user with this email registered'


class IncorrectAccessData(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = 'Incorrect access data'


class TaskNotFound(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = 'Task not found'


class UnauthorizedUser(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = 'Current user is not the task creator'
