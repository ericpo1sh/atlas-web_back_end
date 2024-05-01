#!/usr/bin/env python3
''' Module Documentation '''
from typing import List


def sum_list(input_lists: List[float]) -> float:
    ''' takes a list input_list of floats
    as argument and returns their sum as a float. '''
    sum: float = 0
    for list in input_lists:
        sum += list
    return sum
