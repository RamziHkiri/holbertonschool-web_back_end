#!/usr/bin/env python3
"""class BasicAuth enherit from Auth"""
from typing import List, TypeVar
from models.user import User
from api.v1.auth.auth import Auth
from base64 import b64decode


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """decode_base_64"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_byte = b64decode(base64_authorization_header)
            decoded_string = decoded_byte.decode('utf-8')
            return decoded_string
        except BaseException:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """extract_user_credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        user = decoded_base64_authorization_header.split(':', 1)[0]
        password = decoded_base64_authorization_header.split(':', 1)[1]
        return user, password

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """get user credentials"""
        if user_email is None or type(user_email) != str or\
           user_pwd is None or type(user_pwd) != str:
            return None

        get_users = User.search({'email': user_email})

        try:
            found_users: List[TypeVar('User')]
            found_users = User.search({'email': user_email})
        except Exception:
            return None
        for user in get_users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Overload func to get the info of the user

            Args:
                request: current user

            Return:
                Info of the current user or users, otherwise None
        """
        header: str = self.authorization_header(request)

        if header is None:
            return None

        auth_head64: str = self.extract_base64_authorization_header(header)

        if auth_head64 is None:
            return None

        decode_auth: str = self.decode_base64_authorization_header(auth_head64)

        if decode_auth is None:
            return decode_auth

        mail: str
        passwd: str
        mail, passwd = self.extract_user_credentials(decode_auth)

        if mail is None or passwd is None:
            return None

        user_curr = self.user_object_from_credentials(mail, passwd)

        return user_curr
