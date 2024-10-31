#!/usr/bin/python3
"""Lockboxes module"""


def canUnlockAll(boxes):
    # Initialize a set to keep track of opened boxes
    opened_boxes = set()
    # A queue to hold boxes to explore (start with the first box)
    queue = [0]

    while queue:
        # Get the current box to open
        current_box = queue.pop(0)
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
