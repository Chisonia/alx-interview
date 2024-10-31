#!/usr/bin/python3
"""Lockboxes module"""

from collections import deque


def canUnlockAll(boxes):
    # Initialize a set to keep track of opened boxes
    opened_boxes = set()
    # A deque to hold boxes to explore (start with the first box)
    queue = deque([0])

    while queue:
        # Get the current box to open
        current_box = queue.popleft()  # Use popleft for O(1) complexity
        # If the box has not been opened yet
        if current_box not in opened_boxes:
            # Mark the box as opened
            opened_boxes.add(current_box)
            # Get keys from the current box
            keys = boxes[current_box]
            # Add the keys to the queue if they unlock other boxes
            for key in keys:
                if key < len(boxes) and key not in opened_boxes:
                    queue.append(key)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)


# Sample Test Cases
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False

    # Test case with 1000 boxes with all keys in each box
    boxes_large = [[i for i in range(1000)] for _ in range(1000)]
    print(canUnlockAll(boxes_large))  # True