#!/usr/bin/python3
""" UTF-8 validation """


def validUTF8(data):
    """ main function """
    flag = False
    jump_list = {30: 3, 14: 4, 6: 5}
    char_length = {3: 3, 4: 2, 5: 1}
    list_length = 0
    if len(data) == 0:
        return True
    if len(data) == 1 and data[0] >> 7 == 0:
        return True
    for num in data:
        if list_length:
            list_length -= 1
        else:
            flag = False
        if num >> 7 != 0 and len(bin(num)[2:]) >= 8:
            flag = True
            for test_point, shift in jump_list.items():
                if num >> shift == test_point:
                    list_length = char_length[shift]
                else:
                    return False
        if num >> 7 == 0 and flag:
            return False
    return True
