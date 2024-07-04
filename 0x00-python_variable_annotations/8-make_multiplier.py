#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier
    """
    def multiplies(n: float):
        """
        multiply two number
        """
        return n * multiplier
    return multiplies
