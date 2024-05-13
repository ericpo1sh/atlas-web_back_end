#!/usr/bin/env python3
''' Auth Class Module '''
from flask import request
from typing import List, TypeVar


class Auth:
    ''' create a class to manage the API authentication. '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' that returns False - path and excluded_paths '''
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path + '/' in excluded_paths or path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        ''' returns None - request will be the Flask request object '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' returns None - request will be the Flask request object '''
        return None
