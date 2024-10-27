#!/usr/bin/env python3

"""
A type-annotated function to_kv that takes a string k and an
int OR float v as arguments and returns a tuple.

The first element of the tuple is the string k.

The second element is the square of the int/float v and is
annotated as a float.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns the string and the square of the number"""
    return k, v ** 2
