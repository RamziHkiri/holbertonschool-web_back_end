#!/usr/bin/env python3
"""Write a function called filter_datum that returns
the log message obfuscated.
"""
import re
from typing import List


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
