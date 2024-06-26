#!/usr/bin/env python3
''' Session Auth Class Module '''
from api.v1.auth.auth import Auth
import uuid
from models.user import User
from typing import TypeVar


class SessionAuth(Auth):
    ''' class SessionAuth that inherits from Auth. '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        ''' Creates a session for the User ID '''
        if user_id is None or not isinstance(user_id, str):
            return None
        else:
            session_id = uuid.uuid4()
            self.user_id_by_session_id[str(session_id)] = user_id
            return str(session_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        ''' returns a User ID based on a Session ID: '''
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        ''' returns a User instance based on a cookie value '''
        session_id = self.session_cookie(request)
        if not session_id:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return None
        return User.get(user_id)

    def destroy_session(self, request=None):
        ''' deletes the user session / logout '''
        if request is None:
            return False

        session_cookie = self.session_cookie(request)
        if not session_cookie:
            return False

        user_id = self.user_id_for_session_id(session_cookie)
        if not user_id:
            return False

        del self.user_id_by_session_id[session_cookie]
        return True
