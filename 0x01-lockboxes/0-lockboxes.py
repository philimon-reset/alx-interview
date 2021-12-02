#!/user/bin/python3
def canUnlockAll(boxes):
    T = []
    for i in range(1, len(boxes)):
        order = [T.extend(x) for x in boxes[:i] + boxes[i + 1:]]
        if i in T:
            T = []
        else:
            return False
    return True
