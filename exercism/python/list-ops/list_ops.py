"""
Custom implementations of common list operations.
"""

from collections.abc import Iterable
from typing import Any, Callable


# pylint: disable=redefined-builtin


def append(list1: list, list2: list) -> list:
    """Return a new list containing elements from both lists."""
    return [*list1, *list2]


def concat(lists: list) -> list:
    """Flatten nested iterables into a single list."""
    result = []

    for iterable in lists:
        if isinstance(iterable, Iterable):
            result.extend(iterable)
        else:
            result.append(iterable)

    return result


def filter(function: Callable, items: list) -> list:
    """Return items that satisfy the predicate function."""
    return [item for item in items if function(item)]


def length(items: list) -> int:
    """Return the number of elements in the list."""
    return len(items)


def map(function: Callable, items: list) -> list:
    """Apply a function to every item in the list."""
    return [function(item) for item in items]


def foldl(function: Callable, items: list, initial: Any) -> Any:
    """Reduce the list from left to right."""
    while items:
        initial = function(initial, items.pop(0))

    return initial


def foldr(function: Callable, items: list, initial: Any) -> Any:
    """Reduce the list from right to left."""
    while items:
        initial = function(initial, items.pop())

    return initial


def reverse(items: list) -> list:
    """Return a reversed copy of the list."""
    return items[::-1]