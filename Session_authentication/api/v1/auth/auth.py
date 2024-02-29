#!/usr/bin/env python3
"""create the class auth"""
import os
from typing import List, TypeVar
from flask import request


class Auth():
    """class auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth"""
        if path is None:
            return True
        if path[len(path) - 1] != '/':
            path += '/'
        if excluded_paths == [] or excluded_paths is None:
            return True
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header"""
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user"""
        return None

    def session_cookie(self, request=None):
        """session cookies"""
        if request is None:
            return None
        SESSION_NAME = os.getenv("SESSION_NAME", "_my_session_id")
        return request.cookies.get(SESSION_NAME)
