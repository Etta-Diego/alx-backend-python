#!/usr/bin/env python3

"""
A type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that
multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that multiplies a float (multiplier)
    and returns a Callable[[float], float]."""
    def float_multiplier(number: float) -> float:
        """Function that takes a float and returns a multiplied float"""
        return multiplier * number
    return float_multiplier
