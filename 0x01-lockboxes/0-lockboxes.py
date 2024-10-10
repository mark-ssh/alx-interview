#!/usr/bin/python3
"""A script to determine if all the boxes can be opened"""


def canUnlockAll(boxes):
    # Start with box 0 unlocked
    unlocked = set([0])
    keys = set(boxes[0])  # Start with keys from the first box

    # Traverse the keys, unlocking boxes
    while keys:
        new_key = keys.pop()
        if new_key < len(boxes) and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(boxes[new_key])  # Add keys from the newly unlocked box

    # Check if all boxes are unlocked
    return len(unlocked) == len(boxes)
