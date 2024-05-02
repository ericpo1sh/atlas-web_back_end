#!/usr/bin/env python3
''' Module Documentation '''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' Coroutine will loop 10x asynchronously and wait 1sec '''
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
