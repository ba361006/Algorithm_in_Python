# -*- coding: utf-8 -*-
import os
import sys
from typing import List

import pytest

sys.path.append(os.path.abspath("."))

from src.binary_tree.array_binary_tree import ArrayBinaryTree


@pytest.mark.parametrize(
    "expected_result, empty_tree, values",
    [
        ([10, 5, 21, 0, 9, 13, 28], [0] * 7, [10, 21, 5, 9, 13, 28]),
        (
            [
                53,
                26,
                60,
                6,
                40,
                55,
                0,
                0,
                0,
                35,
                0,
                54,
                58,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                56,
                0,
                0,
                0,
                0,
                0,
            ],
            [0] * 31,
            [53, 26, 60, 55, 40, 6, 35, 54, 58, 56],
        ),
    ],
)
def test_array_binary_tree_success_cases(
    expected_result: List[int], empty_tree: List[int], values: List[int]
) -> None:
    array_binary_tree = ArrayBinaryTree()
    array_binary_tree.generate_tree(empty_tree=empty_tree, values=values)
    assert expected_result == array_binary_tree.tree
