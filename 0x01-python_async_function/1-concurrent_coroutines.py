"""This imports wait_random from the previous 0-basic_async_syntax.py file
and writes an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. It will spawn wait_random n times
with the specified max_delay.
wait_n returns the list of all the delays (float values).
The list of the delays are in ascending order without the use of
sort() because of concurrency.
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    tasks = []
    delays = []

    for index in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
