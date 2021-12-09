#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    flag = False
    if n < 2 or type(n) != int:
        return 0
    for i in range(2, n):
        if (n % i) == 0:
            flag = True
            break
    if flag:
        pass
    else:
        return n
    if n % 2 == 0:
        C = "H"
        jump = C
        orand = 1
    else:
        C = "HHH"
        jump = "H"
        orand = 3
    while len(C) < n:
        if len(C + jump) <= n and n % len(jump + C) == 0:
            orand += 1
            C += jump
            check = len(C)
        else:
            jump = C
            orand += 2
            C += C
            check = len(C)
    return orand
