#!/usr/bin/env python3
"""async_generator: a coroutine that will loop 10 times, each time
asynchronously wait 1 second, then yield a random number between 0 and 10.
Has no arguements
Uses the random module"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    loops = 10
    loop = 0
    while loop < loops:
        """ loop 10 times, wait 1 second, then yields
        a random number between 0 and 10."""
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        loop += 1
