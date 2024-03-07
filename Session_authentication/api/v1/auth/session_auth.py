#!/usr/bin/env python3
"""class SessionAuth that inherits from Auth"""


from typing import Dict, TypeVar
from models.user import User
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """class SessionAuth"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """crate session"""

        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user_id_for session"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """get the current user"""
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """Deletes de user session / logout"""

        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)

        if not user_id:
            return False

        try:
            del self.user_id_by_session_id[session_id]
        except Exception:
            return False

        return True
