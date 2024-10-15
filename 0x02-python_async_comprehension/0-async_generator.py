#!/usr/bin/env python3
"""async_generator: a coroutine that will loop 10 times, each time
asynchronously wait 1 second, then yield a random number between 0 and 10.
Has no arguements
Uses the random module"""


import asyncio
import random


async def async_generator():
    loops = 10
    loop = 0
    while loop < loops:
        yield random.uniform(0, 10)
        # loop += 1
        # waits 1 sec 
        await asyncio.sleep(1)
        loop += 1
