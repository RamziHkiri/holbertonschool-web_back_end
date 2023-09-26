#!/usr/bin/env python3
"""Python - Async Comprehension task 1 """

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers."""

    return [n async for n in async_generator()]
    """async for i in async_generator():
        result.append(i)"""
    return result
