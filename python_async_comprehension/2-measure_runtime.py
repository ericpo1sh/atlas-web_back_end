#!/usr/bin/env python3
''' Moduel Docstring '''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' measure the total run time '''
    start = time.time()
    await asyncio.gather(
      async_comprehension(),
      async_comprehension(),
      async_comprehension(),
      async_comprehension()
        )
    end = time.time()
    total = end - start
    return total
