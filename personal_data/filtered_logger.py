#!/usr/bin/env python3
"""
Filtered Logger file
"""
import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """ function that returns the log message obfuscated """
    return re.sub(
        r'(' + '|'.join(fields) + r')=[^' + re.escape(separator) + r']*',
        lambda match: match.group(1) + '=' + redaction,
        message
    )
