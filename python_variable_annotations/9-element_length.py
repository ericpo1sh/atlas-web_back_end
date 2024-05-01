#!/usr/bin/env python3
''' Module Documentation '''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Annotate the below function’s parameters '''
    return [(i, len(i)) for i in lst]
