#!/usr/bin/env python3
"""Python - Async Comprehension task 0"""

import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """Wait a second then yield a random number between 0 and 10, 10 times"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
