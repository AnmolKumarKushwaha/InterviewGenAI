"""
=========================================================
File: exceptions.py

Purpose:
    Defines custom exceptions used across the application.
=========================================================
"""


class AppException(Exception):
    """
    Base exception for the application.
    """

    def __init__(self, message: str, error_code: str):
        self.message = message
        self.error_code = error_code
        super().__init__(message)


class AuthenticationException(AppException):

    def __init__(self, message="Authentication Failed"):
        super().__init__(message, "AUTHENTICATION_ERROR")


class AuthorizationException(AppException):

    def __init__(self, message="Access Denied"):
        super().__init__(message, "AUTHORIZATION_ERROR")


class ValidationException(AppException):

    def __init__(self, message="Validation Failed"):
        super().__init__(message, "VALIDATION_ERROR")


class FileUploadException(AppException):

    def __init__(self, message="File Upload Failed"):
        super().__init__(message, "FILE_UPLOAD_ERROR")


class DatabaseException(AppException):

    def __init__(self, message="Database Error"):
        super().__init__(message, "DATABASE_ERROR")


class AIException(AppException):

    def __init__(self, message="AI Service Error"):
        super().__init__(message, "AI_ERROR")