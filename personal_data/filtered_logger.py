#!/usr/bin/env python3
"""Write a function called filter_datum that returns
the log message obfuscated.
"""
import re


def filter_datum(fields, redaction, message, separator):
    """"""
    for field in fields:
        message = re.sub(fr"{field}=([^\{separator}]*){separator}",
                         f"{field}={redaction}{separator}", message)
    return message
