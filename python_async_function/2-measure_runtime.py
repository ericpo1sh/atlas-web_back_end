#!/usr/bin/env python3
''' Module Documentation '''
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Function that measures total execution time for wait_n '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    final_time = end_time - start_time
    return final_time
