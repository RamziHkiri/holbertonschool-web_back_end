#!/usr/bin/env python3
"""Python - Async task 0"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ asynchronous coroutine that waits for a random delay and return it"""

    dela = max_delay * random.random()
    await asyncio.sleep(dela)
    return dela
