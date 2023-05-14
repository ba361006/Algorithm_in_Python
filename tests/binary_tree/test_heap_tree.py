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
def test_array_heap_tree_success_case(
    values: List[int], min_expected_result: List[int], max_expected_result: List[int]
) -> None:
    array_heap_tree = ArrayHeapTree(values)
    assert min_expected_result == array_heap_tree.build_min_heapify()
    assert max_expected_result == array_heap_tree.build_max_heapify()
