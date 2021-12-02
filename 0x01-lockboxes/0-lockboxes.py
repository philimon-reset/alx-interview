#!/user/bin/python3

"""
  Lockboxes: Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
      LockBoxes Function: Return True if all boxes can be opened, else false
    """
    T = []
    for i in range(1, len(boxes)):
        order = [T.extend(x) for x in boxes[:i] + boxes[i + 1:]]
        if i in T:
            T = []
        else:
            return False
    return True
