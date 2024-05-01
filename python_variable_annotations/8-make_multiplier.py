#!/usr/bin/env python3
''' Module Documentation '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' first parameter is a float and
    it returns a func that multiplies by float '''
    def multi(num: float) -> float:
        return num * multiplier
    return multi
