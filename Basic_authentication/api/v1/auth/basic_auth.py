#!/usr/bin/env python3
"""class BasicAuth enherit from Auth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class BasicAuth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract base64"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        second_part = authorization_header.split(' ', 1)[1]
        return second_part
