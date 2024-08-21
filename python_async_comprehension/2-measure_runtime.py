#!/usr/bin/env python3
"""Import async_comprehension from the previous file and write
a measure_runtime ncoroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it"""


import time
import asyncio
comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """measure the total runtime and return it"""
    start = time.perf_counter()
    await asyncio.gather(*(comprehension() for cpt in range(4)))
    end = time.perf_counter()
    return end - start
