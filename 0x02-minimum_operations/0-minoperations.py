#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    if n < 2:
        return 0
    if n % 2 == 0:
        C = "H"
        jump = C
        orand = 0
    else:
        C = "HHH"
        jump = "H"
        orand = 3
    while len(C) < n:
        if len(C + jump) <= n and len(C + C) > n:
            orand += 1
            C += jump
        else:
            jump = C
            orand += 2
            C += C
    return orand
