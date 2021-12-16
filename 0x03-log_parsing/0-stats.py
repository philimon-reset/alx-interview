
#!/usr/bin/python3
""" Log parser projec """


import sys
import re


def print_leftover(file_S):
    """ print the leftovers """
    print(f"File size: {file_S}")
    for key, value in status.items():
        if value != 0:
            print(f"{key}: {value}")

if __name__ == '__main__':
    match_B = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')  # nopep8
    cursor = 0
    file_S = 0
    status = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0}
    try:
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
    finally:
        print_leftover(file_S)