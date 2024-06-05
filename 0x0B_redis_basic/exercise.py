#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    ''' method to count the ammount of times cache is called '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' wrapper function '''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    ''' method to store history of inputs and outputs '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' wrapper function '''
        input_key = f'{method.__qualname__}:inputs'
        output_key = f'{method.__qualname__}:outputs'
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


def replay(method: Callable):
    ''' display the calls of a specified function '''
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"
    inputs = method.__self__._redis.lrange(input_key, 0, -1)
    outputs = method.__self__._redis.lrange(output_key, 0, -1)
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for input_args, output in zip(inputs, outputs):
        print(
            f"{method.__qualname__}(*{input_args.decode('utf-8')})"
            f" -> {output.decode('utf-8')}")


class Cache:
    ''' Cache Class '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def get_count_call(self, method_name: str) -> int:
        ''' method to get the call count for methods '''
        key = f"{self.__class__.__name__}.{method_name}:calls"
        count = self._redis.get(key)
        return int(count) if count else 0
