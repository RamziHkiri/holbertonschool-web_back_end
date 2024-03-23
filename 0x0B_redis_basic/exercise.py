#!/usr/bin/env python3
"""implement the class Cache"""

from typing import Callable, Optional, Union
from uuid import uuid4
import redis


class Cache:
    """ Class for implementing a Cache """

    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

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
