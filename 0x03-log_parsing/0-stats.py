#!/usr/bin/python3
""" Log parser project """


import random
import sys
from time import sleep
import re
import signal

match_B = re.compile("""\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d{1,4})""")  # nopep8
status = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0}


def signal_handler():
    """ signal handler """
    cursor = 0
    file_S = 0
    for i in sys.stdin:
        result = re.match(match_B, i)
        if result:
            cursor += 1
            status[result.group(1)] += 1
            file_S += int(result.group(2))
            if cursor % 10 == 0:
                print(f"File size: {file_S}")
                for key, value in status.items():
                    if value != 0:
                        print(f"{key}: {value}")
    return file_S


def print_leftover(file_S):
    """ print the leftovers """
    print(f"File size: {file_S}")
    for key, value in status.items():
        if value != 0:
            print(f"{key}: {value}")

if __name__ == '__main__':
    try:
        file = signal_handler()
    finally:
        print_leftover(file)
