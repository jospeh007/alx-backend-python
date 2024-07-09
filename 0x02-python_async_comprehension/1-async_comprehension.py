#!/usr/bin/env python3
""" Async Comprehensions """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async generator list of float """
    return [_ async for _ in async_generator()]
