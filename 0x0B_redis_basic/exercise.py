#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    ''' Cache Class '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' method to store things '''
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self,
            key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        ''' get method '''
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        ''' method to automatically parametrize cache.get str conversion '''
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: int) -> Optional[int]:
        ''' method to automatically parametrize cache.get int conversion '''
        return self.get(key, fn=int)
