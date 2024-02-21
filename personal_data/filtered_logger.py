#!/usr/bin/env python3
"""Write a function called filter_datum that returns
the log message obfuscated.
"""
from typing import List
import re
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    function called filter_datum that returns the log message obfuscated

    Args:
        fields (list[str]): _description_
        redaction (str): _description_
        message (str): _description_
        separator (str): _description_

    Returns:
        str: _description_
    """
    for field in fields:
        message = re.sub(fr"{field}=([^\{separator}]*){separator}",
                         f"{field}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
