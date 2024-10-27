#!/usr/bin/env python3

"""
Annotates the below function’s parameters and
return values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]
"""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotates function’s parameters and
return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
