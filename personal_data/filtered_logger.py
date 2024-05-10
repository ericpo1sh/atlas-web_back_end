#!/usr/bin/env python3
"""
Filtered Logger file
"""
import re
import logging
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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        ''' modified class to accept fields as an arguement '''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        ''' implemented method to filter incoming log records using func '''
        filter_datum(self.fields, self.REDACTION, )
        NotImplementedError

