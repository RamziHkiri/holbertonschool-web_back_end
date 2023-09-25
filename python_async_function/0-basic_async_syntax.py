#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    dela = max_delay * random.random()
    await asyncio.sleep(dela)
    return dela
