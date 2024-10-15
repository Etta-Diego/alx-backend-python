#!/usr/bin/env python3
"""Imports async_comprehension from the 1-async_comprehension.pyfile."""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

"""Measure_runtime: a coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
It measures the total runtime and return it."""


async def measure_runtime():
    """Starts the timer"""
    start_time = time.perf_counter()
    """Run async_comprehension four times in parallel"""
    await asyncio.gather(*(async_comprehension()
        for i in range(4)))
    """Stops the timer"""
    end_time = time.perf_counter()
    total_runtime = end_time - start_time
    return total_runtime

