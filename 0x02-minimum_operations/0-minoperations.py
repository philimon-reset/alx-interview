#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    flag = False
    if n < 2:
        return 0
    for i in range(2, n):
        if (n % i) == 0:
            factor = i
            flag = True
            break
    if flag:
        pass
    else:
        return n
    orand = factor
    C = "H" * factor
    jump = "H"
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

if __name__ == '__main__':
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 25
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
