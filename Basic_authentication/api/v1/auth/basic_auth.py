#!/usr/bin/env python3
''' Basic Auth Class Module '''
from api.v1.auth.auth import Auth
import base64


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
