"""Week 5 homework: Midnight Mail Train.

Complete the required functions and classes.
Use recursion only where the instructions require recursion.
"""

from __future__ import annotations


class TrainCarNode:
    """A node in a doubly linked list of train cars."""

    def __init__(self, car_id: str) -> None:
        self.car_id = car_id
        self.prev: TrainCarNode | None = None
        self.next: TrainCarNode | None = None


class MidnightMailDLL:
    """A doubly linked list for train cars."""

    def __init__(self) -> None:
        self.head: TrainCarNode | None = None
        self.tail: TrainCarNode | None = None

    def append_car(self, car_id: str) -> None:
        """Add a train car to the end of the list."""
        new_node = TrainCarNode(car_id)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def detach_last_car(self) -> str | None:
        """Remove the last train car and return its ID.

        Return None if the list is empty.
        """
        if self.tail is None:
            return None
        car_id = self.tail.car_id
        if self.tail.prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return car_id

    def to_reverse_list(self) -> list[str]:
        """Return all train car IDs from tail to head."""
        result = []
        current = self.tail
        while current is not None:
            result.append(current.car_id)
            current = current.prev
        return result


def is_valid_ticket_code(code: str) -> bool:
    """Return True only if the code starts with 'MM-' and ends with exactly 4 digits."""
    if not code.startswith("MM-"):
        return False
    suffix = code[3:]
    return len(suffix) == 4 and suffix.isdigit()


def count_priority_labels(labels: list[str], target: str) -> int:
    """Recursively count how many times target appears in labels."""
    if not labels:
        return 0
    match = 1 if labels[0] == target else 0
    return match + count_priority_labels(labels[1:], target)


def clean_radio_message(message: str) -> str:
    """Recursively return a new string with all spaces removed."""
    if not message:
        return ""
    first = "" if message[0] == " " else message[0]
    return first + clean_radio_message(message[1:])


# Optional stretch

def count_priority_labels_iterative(labels: list[str], target: str) -> int:
    """Optional stretch: iterative version of count_priority_labels."""
    return sum(1 for label in labels if label == target)


def clean_radio_message_iterative(message: str) -> str:
    """Optional stretch: iterative version of clean_radio_message."""
    return message.replace(" ", "")