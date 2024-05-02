#!/usr/bin/python3
"""
This module contains a function that checks a sequence of boxes if they can
be opened or not
"""


def canUnlockAll(boxes):
    """
    This function checks if a list of boxes can be opened or not
    """
    if not boxes or len(boxes) == 0 or not isinstance(boxes, list):
        return False

    keys = set([0])
    keys_to_check = [0]

    while keys_to_check:
        key = keys_to_check.pop()
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.add(box)
                keys_to_check.append(box)

    if len(keys) == len(boxes):
        return True
    return False
