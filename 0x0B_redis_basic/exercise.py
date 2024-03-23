#!/usr/bin/env python3
"""implement the class Cache"""

import functools
from typing import Callable, Optional, Union
from uuid import uuid4
import redis


def call_history(method: Callable) -> Callable:
    """ Decorator to store the history of inputs and
    outputs for a particular function.
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper for decorator functionality """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper


def replay(method: Callable):
    """ replay to display hstory of calls"""
    self_ = method.__self__
    stored_name = method.__qualname__
    stored_key = self_.get(stored_name)
    if stored_key:
        times = self_.get_str(stored_key)
        inputs = self_._redis.lrange(stored_name + ":inputs", 0, -1)
        outputs = self_._redis.lrange(stored_name + ":outputs", 0, -1)

        print(f"{stored_name} was called {times} times:")
        zipvalues = zip(inputs, outputs)
        result_list = list(zipvalues)
        for k, v in result_list:
            name = self_.get_str(k)
            val = self_.get_str(v)
            print(f"{stored_name}(*{name}) -> {val}")


def count_calls(method: Callable) -> Callable:
    """ Decortator for counting how many times a function
    has been called """

    key = method.__qualname__

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper for decorator functionality """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """ Class for implementing a Cache """

    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a
        random key and return the key.
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Reading from Redis and recovering original type """
        value = self._redis.get(key)
        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """ Parameterizes a value from redis to str """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Parameterizes a value from redis to int """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
