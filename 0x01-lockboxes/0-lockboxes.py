#!/usr/bin/python3

"""
  Lockboxes
  You have n number of locked boxes in front of you.
  Each box is numbered sequentially from 0 to n - 1
  and each box may contain keys to the other boxes.
  Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
      Implementation
    """

    keys = [] + boxes[0]
    need_keys = []

    for box in range(1, len(boxes)):
        if not keys:
            return False
        if box in keys:
            keys = keys + boxes[box]
            for box_prev in need_keys:
                if box_prev in keys:
                    keys = keys + boxes[box_prev]
                    need_keys.pop(need_keys.index(box_prev))
        else:
            need_keys.append(box)
    if not need_keys:
        return True
    else:
        return False
