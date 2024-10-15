#!/usr/bin/env python3
"""This contains an asynchronous coroutine that takes in an integer
argument (max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay (included
and float value) seconds and eventually returns it.

It uses the random module.
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    # waits for  a random delay
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
