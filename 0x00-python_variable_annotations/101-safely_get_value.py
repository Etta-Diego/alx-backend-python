#!/usr/bin/env python3

"""
Add type annotations to the function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""

from typing import Union, Any, Mapping, TypeVar

"""Initialize TypeVar to T"""
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """ Added type annotations to the function """
    if key in dct:
        return dct[key]
    else:
        return default
