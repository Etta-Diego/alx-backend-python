#!/usr/bin/env python3

"""
A type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """sums a list of integer and floats"""
    total = 0.0
    for num in mxd_lst:
        total += num
    return total
