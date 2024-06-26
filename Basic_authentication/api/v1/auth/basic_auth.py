#!/usr/bin/env python3
''' Basic Auth Class Module '''
from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    ''' class BasicAuth that inherits from Auth. '''
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        ''' returns the Base64 part of the Authorization header '''
        if authorization_header is None:
            return None
        elif not isinstance(authorization_header, str):
            return None
        elif not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        ''' returns the decoded value of a Base64 string '''
        if base64_authorization_header is None:
            return None
        elif not isinstance(base64_authorization_header, str):
            return None
        try:
            # Decode the Base64 encoded string
            decoded_bytes = base64.b64decode(base64_authorization_header)
            # Convert the bytes to a UTF-8 string
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except (base64.binascii.Error, UnicodeDecodeError):
            # Return None if there is an error in decoding
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        ''' returns user email and password from the Base64 decoded value. '''
        if decoded_base64_authorization_header is None:
            return None, None
        elif not isinstance(decoded_base64_authorization_header, str):
            return None, None
        elif ":" not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':')
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        ''' returns the User instance based on email and password. '''
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        elif user_email is None or user_pwd is None:
            return None
        try:
            users = User.search({"email": user_email})
        except Exception:
            return None
        if users is None:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
            else:
                return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''  overloads Auth and retrieves the User instance for a request '''
        if request is None:
            return None

        header = request.headers.get('Authorization')
        base64_header = self.extract_base64_authorization_header(header)
        decoded_header = self.decode_base64_authorization_header(base64_header)
        user_email, user_pwd = self.extract_user_credentials(decoded_header)

        return self.user_object_from_credentials(user_email, user_pwd)
