#!/usr/bin/env python3
''' Moduel Docstring '''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' measure the total run time '''
    start = time.time()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    total = end - start
    return total
