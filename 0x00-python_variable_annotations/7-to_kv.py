#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int] -> Tuple[str, float]:
        """
        Return str or float
        """
        return (k, v**2)
