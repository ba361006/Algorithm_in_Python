# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.abspath("."))

from typing import List
import pytest
from src.tree.array_heap_tree import ArrayHeapTree


@pytest.mark.parametrize(
    "values, min_expected_result, max_expected_result",
    (
        [
            [10, 21, 5, 9, 13, 28, 3],
            [3, 9, 5, 21, 13, 28, 10],
            [28, 21, 10, 9, 13, 5, 3],
        ],
        [
            [53, 26, 60, 55, 40, 6, 35, 54, 58, 56],
            [6, 26, 35, 54, 40, 60, 53, 55, 58, 56],
            [60, 58, 53, 55, 56, 6, 35, 54, 26, 40],
        ],
    ),
)
def test_array_heap_tree_build_success_case(
    values: List[int], min_expected_result: List[int], max_expected_result: List[int]
) -> None:
    array_heap_tree = ArrayHeapTree(values)
    assert min_expected_result == array_heap_tree.build_min_heapify()
    assert max_expected_result == array_heap_tree.build_max_heapify()


@pytest.mark.parametrize(
    "values, value, expected_result",
    (
        [
            [10, 21, 5, 9, 13, 28, 3],
            25,
            [3, 9, 5, 21, 13, 28, 10, 25],
        ],
        [
            [53, 26, 60, 55, 40, 6, 35, 54, 58, 56],
            25,
            [6, 25, 35, 54, 26, 60, 53, 55, 58, 56, 40],
        ],
    ),
)
def test_array_heap_tree_min_heap_push_success_case(
    values: List[int], value: int, expected_result: List[int]
) -> None:
    array_heap_tree = ArrayHeapTree(values)
    assert expected_result == array_heap_tree.min_heap_push(value)


@pytest.mark.parametrize(
    "values, value, expected_result",
    (
        [
            [10, 21, 5, 9, 13, 28, 3],
            25,
            [28, 25, 10, 21, 13, 5, 3, 9],
        ],
        [
            [53, 26, 60, 55, 40, 6, 35, 54, 58, 56],
            25,
            [60, 58, 53, 55, 56, 6, 35, 54, 26, 40, 25],
        ],
    ),
)
def test_array_heap_tree_max_heap_push_success_case(
    values: List[int], value: int, expected_result: List[int]
) -> None:
    array_heap_tree = ArrayHeapTree(values)
    assert expected_result == array_heap_tree.max_heap_push(value)


@pytest.mark.parametrize(
    "values, expected_result",
    (
        [
            [10, 21, 5, 9, 13, 28, 3],
            (3, [5, 9, 10, 21, 13, 28]),
        ],
        [
            [53, 26, 60, 55, 40, 6, 35, 54, 58, 56],
            (6, [26, 40, 35, 54, 56, 60, 53, 55, 58]),
        ],
    ),
)
def test_array_heap_tree_min_heap_pop_success_case(
    values: List[int], expected_result: List[int]
) -> None:
    array_heap_tree = ArrayHeapTree(values)
    assert expected_result == array_heap_tree.min_heap_pop()


@pytest.mark.parametrize(
    "values, expected_result",
    (
        [
            [10, 21, 5, 9, 13, 28, 3],
            (28, [21, 13, 10, 9, 3, 5]),
        ],
        [
            [53, 26, 60, 55, 40, 6, 35, 54, 58, 56],
            (60, [58, 56, 53, 55, 40, 6, 35, 54, 26]),
        ],
    ),
)
def test_array_heap_tree_max_heap_pop_success_case(
    values: List[int], expected_result: List[int]
) -> None:
    array_heap_tree = ArrayHeapTree(values)
    assert expected_result == array_heap_tree.max_heap_pop()


@pytest.mark.parametrize(
    "values, value, expected_result",
    (
        [[10, 21, 5, 9, 13, 28, 3], 11, (3, [5, 9, 10, 21, 13, 28, 11])],
        [
            [53, 26, 60, 55, 40, 6, 35, 54, 58, 56],
            11,
            (6, [11, 26, 35, 54, 40, 60, 53, 55, 58, 56]),
        ],
    ),
)
def test_array_heap_tree_min_push_pop_success_case(
    values: List[int], value: int, expected_result: List[int]
) -> None:
    array_heap_tree = ArrayHeapTree(values)
    assert expected_result == array_heap_tree.min_push_pop(value)


@pytest.mark.parametrize(
    "values, value, expected_result",
    (
        [[10, 21, 5, 9, 13, 28, 3], 11, (28, [21, 13, 11, 9, 3, 5, 10])],
        [
            [53, 26, 60, 55, 40, 6, 35, 54, 58, 56],
            11,
            (60, [58, 56, 53, 55, 40, 6, 35, 54, 26, 11]),
        ],
    ),
)
def test_array_heap_tree_max_push_pop_success_case(
    values: List[int], value: int, expected_result: List[int]
) -> None:
    array_heap_tree = ArrayHeapTree(values)
    assert expected_result == array_heap_tree.max_push_pop(value)
