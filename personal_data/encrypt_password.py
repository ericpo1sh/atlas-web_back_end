#!/usr/bin/env python3
"""
Encrypt password using bcrypt
"""
import bcrypt


def hash_password(password: str) -> bytes:
    ''' function that uses bcrypt and returns a hashed password '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    ''' Check valid password  '''
    if bcrypt.checkpw(hashed_password, password):
        return True
    else:
        return False
