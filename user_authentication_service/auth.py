#!/usr/bin/env python3
""" Auth Model """
import bcrypt


def _hash_password(password: str) -> bytes:
    '''  method that takes in a password
    string arguments and returns bytes. '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
