#!/usr/bin/env python3
""" Auth Model """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        ''' take mandatory email and password
        string arguments and return a User object. '''
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pw = self._hash_password(password)
            create_user = self._db.add_user(email, hashed_pw)
            return create_user

    def _hash_password(self, password: str) -> bytes:
        '''  method that takes in a password
        string arguments and returns bytes. '''
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
