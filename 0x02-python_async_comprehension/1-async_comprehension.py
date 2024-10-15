#!/usr/bin/env python3
"""Import async_generator from 0-async_generator.py file"""

from typing import List
async_generator = __import__('0-async_generator').async_generator
"""
async_comprehension: This coroutine will collect 10 random numbers
using an async comprehensing over async_generator,
then returns the 10 random numbers.
It takes no arguments."""


async def async_comprehension() -> List[float]:
    """Use an async comprehension to collect all 10 numbers into a list."""
    return [rand_num async for rand_num in async_generator()]
