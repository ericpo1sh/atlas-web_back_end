#!/usr/bin/env python3
''' Module Documentation '''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' function that executes multiple coroutines at the same time '''
    delay = [task_wait_random(max_delay) for i in range(n)]
    delay_list = await asyncio.gather(*delay)

    return (sorted(delay_list))
