#!/usr/bin/env python3
''' Module Documentation '''
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' function that executes multiple coroutines at the same time '''
    delay = [wait_random(max_delay) for i in range(n)]
    delay_list = await asyncio.gather(*delay)

    return (sorted(delay_list))
