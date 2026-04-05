from src.challenges import (
    MidnightMailDLL,
    clean_radio_message,
    count_priority_labels,
    is_valid_ticket_code,
)


# Problem 1: DLL

def test_append_and_reverse_list_basic() -> None:
    train = MidnightMailDLL()
    train.append_car("A1")
    train.append_car("B2")
    train.append_car("C3")
    assert train.to_reverse_list() == ["C3", "B2", "A1"]


def test_detach_last_car_basic() -> None:
    train = MidnightMailDLL()
    train.append_car("A1")
    train.append_car("B2")
    assert train.detach_last_car() == "B2"
    assert train.to_reverse_list() == ["A1"]


def test_detach_last_car_empty() -> None:
    train = MidnightMailDLL()
    assert train.detach_last_car() is None


# Problem 2: ticket code

def test_ticket_code_valid_example() -> None:
    assert is_valid_ticket_code("MM-1234") is True

def test_ticket_code_invalid_prefix() -> None:
    assert is_valid_ticket_code("XX-1234") is False

def test_ticket_code_invalid_too_many_digits() -> None:
    assert is_valid_ticket_code("MM-12345") is False

def test_ticket_code_edge_letters_instead_of_digits() -> None:
    assert is_valid_ticket_code("MM-abcd") is False


# Problem 3: recursion on a list

def test_count_priority_labels_basic() -> None:
    labels = ["PRIORITY", "NORMAL", "PRIORITY", "LATE"]
    assert count_priority_labels(labels, "PRIORITY") == 2

def test_count_priority_labels_empty() -> None:
    assert count_priority_labels([], "PRIORITY") == 0

def test_count_priority_labels_no_match() -> None:
    labels = ["NORMAL", "LATE", "NORMAL"]
    assert count_priority_labels(labels, "PRIORITY") == 0

def test_count_priority_labels_all_match() -> None:
    labels = ["PRIORITY", "PRIORITY", "PRIORITY"]
    assert count_priority_labels(labels, "PRIORITY") == 3


# Problem 4: recursion on a string

def test_clean_radio_message_basic() -> None:
    assert clean_radio_message("go now") == "gonow"

def test_clean_radio_message_empty() -> None:
    assert clean_radio_message("") == ""

def test_clean_radio_message_no_spaces() -> None:
    assert clean_radio_message("SOS") == "SOS"

def test_clean_radio_message_only_spaces() -> None:
    assert clean_radio_message("   ") == ""