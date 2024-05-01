#!/usr/bin/env python3
''' Module Documentation '''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    ''' Function that waits for delay then returns the delay time '''
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
