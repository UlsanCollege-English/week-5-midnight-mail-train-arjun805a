# Week 5: Midnight Mail Train

## Summary

This project builds small tools for a late-night rail delivery company. It covers a doubly linked list for managing train cars, a ticket code validator, and two recursive functions for counting labels and cleaning radio messages.

## Approach

### Problem 1 — Train Cars DLL

`MidnightMailDLL` is a doubly linked list where each `TrainCarNode` holds a `car_id` and pointers to both the previous and next node. Keeping a `tail` pointer makes `append_car` and `detach_last_car` O(1) — no traversal needed. `to_reverse_list` walks backwards from `tail` using `.prev` links.

### Problem 2 — Ticket Code Check

`is_valid_ticket_code` uses `str.startswith` to check the `"MM-"` prefix, then slices the remainder and checks that it is exactly 4 characters long and all digits with `isdigit()`. No regex needed.

### Problem 3 — Count Priority Labels (Recursion)

**Base case:** empty list → return 0.  
**Recursive step:** check if the first element matches the target (1 or 0), then add the result of calling the function on the rest of the list.

### Problem 4 — Clean Radio Message (Recursion)

**Base case:** empty string → return `""`.  
**Recursive step:** if the first character is a space, skip it; otherwise keep it. Concatenate with the result of calling the function on the remaining string.

### Stretch — Iterative Versions

Both iterative versions are included in `src/challenges.py`.

- `count_priority_labels_iterative` uses a generator expression inside `sum()`.
- `clean_radio_message_iterative` uses `str.replace(" ", "")`.

**Comparison:**

| | Recursive | Iterative |
|---|---|---|
| Clarity | Clear intent, mirrors the problem definition | Shorter, more Pythonic |
| Call stack space | O(n) — one frame per element/character | O(1) — no stack growth |
| Risk | Stack overflow on very large inputs | None |

The iterative versions are safer for large inputs. The recursive versions are closer to how the problem is described and make the base case and step explicit, which is useful for learning.

## Complexity

| Function | Time | Space |
|---|---|---|
| `append_car` | O(1) | O(1) |
| `detach_last_car` | O(1) | O(1) |
| `to_reverse_list` | O(n) | O(n) |
| `is_valid_ticket_code` | O(1) | O(1) |
| `count_priority_labels` | O(n) | O(n) call stack |
| `clean_radio_message` | O(n) | O(n) call stack + result string |

`to_reverse_list` is O(n) in both time and space because it visits every node and builds a new list. The recursive functions are O(n) in space due to call stack frames — one frame per element or character.

## Edge-Case Checklist

### DLL
- [x] Empty train — `detach_last_car` returns `None`, `to_reverse_list` returns `[]`
- [x] Single car — detach leaves list fully empty (`head` and `tail` both `None`)
- [x] Multiple cars — reverse list returns correct order

### Ticket Code
- [x] Valid — `"MM-1234"` → `True`
- [x] Wrong prefix — `"XX-1234"` → `False`
- [x] Too many digits — `"MM-12345"` → `False`
- [x] Too few digits — `"MM-12"` → `False`
- [x] Letters instead of digits — `"MM-abcd"` → `False`
- [x] Empty string — `""` → `False`

### Count Priority Labels
- [x] Empty list → `0`
- [x] No matches → `0`
- [x] All match → full count
- [x] Mixed list → correct count

### Clean Radio Message
- [x] Empty string → `""`
- [x] No spaces → unchanged
- [x] Only spaces → `""`
- [x] Leading and trailing spaces → removed

## Assistance & Sources

- Course slides — Week 5 (Recursion, Linked Lists)
- Python docs — [`str.isdigit`](https://docs.python.org/3/library/stdtypes.html#str.isdigit), [`str.startswith`](https://docs.python.org/3/library/stdtypes.html#str.startswith)
- No AI assistance used