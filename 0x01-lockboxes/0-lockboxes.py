#!/usr/bin/python3
"""model file for Lockboxes"""


def canUnlockAll(boxes):
    """find if all the boxes can be opened"""
    if boxes is None:
        return False
    if len(boxes) >= 1:
        if len(boxes) == 0:
            return False
        return True
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    return len(keys) == len(boxes)
