#!/usr/bin/env python3
"""Write a function called filter_datum that returns
the log message obfuscated.
"""


def filter_datum(fields, redaction, message, separator):
    pairs = message.split(separator)

    data = {}
    filtred_message = ''
    for pair in pairs:
        if "=" in pair:
            key, value = pair.split("=")
            data[key] = value

    for field in fields:
        for key, value in data.items():
            if key == field:
                data[key] = redaction

    for key, value in data.items():
        filtred_message += + key + "=" + value + separator

    return filtred_message
