# -*- coding: utf-8 -*-
import os
import sys
from typing import List
from typing import Optional

import pytest

sys.path.append(os.path.abspath("."))

from src.binary_tree.array_binary_tree import ArrayBinaryTree
from src.binary_tree.linked_list_binary_tree import Node, LinkedListBinaryTree


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


def test_linked_list_binary_tree_success() -> None:
    def inorder_travser(output: List[Optional[int]], node: Node) -> None:
        if node.left:
            inorder_travser(output, node.left)
        output.append(node.value)
        if node.right:
            inorder_travser(output, node.right)

    linked_list_binary_tree = LinkedListBinaryTree()
    node_values = [10, 21, 5, 9, 13, 28]
    for value in node_values:
        linked_list_binary_tree.insert(Node(value))

    result: List[Optional[int]] = []
    expected_result = [5, 9, 10, 13, 21, 28]
    inorder_travser(result, linked_list_binary_tree.root)
    assert expected_result == result
