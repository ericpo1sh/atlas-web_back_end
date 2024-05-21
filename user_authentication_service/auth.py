#!/usr/bin/env python3
""" Auth Model """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import uuid


def _hash_password(self, password: str) -> bytes:
    '''  method that takes in a password
    string arguments and returns bytes. '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    ''' function that generates a new uuid '''
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        '''  method that takes in a password
        string arguments and returns bytes. '''
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        ''' take mandatory email and password
        string arguments and return a User object. '''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            user = None
        if user:
            raise ValueError(f"User {email} already exists")
        else:
            hashed_password = self._hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        ''' Function for Credentials validation '''
        try:
            user = self._db.find_user_by(email=email)
            if user:
                if bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password):
                    return True
        except NoResultFound:
            pass
        except InvalidRequestError:
            pass
        return False

    def _generate_uuid() -> str:
        ''' function that generates a new uuid '''
        return str(uuid.uuid4())

    def create_session(self, email: str) -> str:
        ''' find the user corresponding to the email,
        generate a new UUID and store it in the database
        as the user’s session_id, then return the session ID. '''
        try:
            user = self._db.find_user_by(email=email)
            if user:
                user.session_id = _generate_uuid()
                return str(user.session_id)
        except NoResultFound:
            pass
        except InvalidRequestError:
            pass

    def get_user_from_session_id(self, session_id: str):
        ''' Function that Finds user by session ID  '''
        try:
            user = self._db.find_user_by(session_id=session_id)
            if user:
                return user
        except NoResultFound:
            pass
        except InvalidRequestError:
            pass
        return None

    def destroy_session(self, user_id: int) -> None:
        ''' Function that updates the user’s session ID to None. '''
        if user_id is not None:
            try:
                self._db.update_user(user_id=user_id, session_id=None)
            except NoResultFound:
                pass
            except InvalidRequestError:
                pass

    def get_reset_password_token(self, email: str) -> str:
        ''' Generate reset password token  '''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        new_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=new_token)
        return new_token

    def update_password(self, reset_token: str, password: str) -> None:
        ''' Uses the reset_token to find the corresponding user
        and updates their hashed password '''
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        new_password = _hash_password(password)
        self._db.update_user(user.id, new_password=new_password)
        self._db.update_user(user.id, reset_token=None)
        return None
