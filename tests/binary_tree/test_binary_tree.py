# -*- coding: utf-8 -*-
import io
import os
import sys
from copy import deepcopy
from typing import Callable
from typing import List
from typing import Optional

import pytest

sys.path.append(os.path.abspath("."))

from src.binary_tree.array_binary_tree import ArrayBinaryTreeGenerator
from src.binary_tree.linked_list_binary_tree import Node


def get_text_from_stdout(printing_function: Callable[[], None]) -> List[int]:
    # Save the current stdout stream
    original_stdout = sys.stdout

    # Create a new stream to capture the output
    output = io.StringIO()
    sys.stdout = output

    # Call the function that prints some text
    printing_function()

    # Reset the stdout stream
    sys.stdout = original_stdout

    # Get the printed text as a string
    raw_text = output.getvalue()

    return list(map(int, raw_text.split()))


@pytest.mark.parametrize(
    "expected_result, values",
    [
        ([10, 5, 21, 0, 9, 13, 28], [10, 21, 5, 9, 13, 28]),
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
            ],
            [53, 26, 60, 55, 40, 6, 35, 54, 58, 56],
        ),
    ],
)
def test_array_binary_tree_success_cases(
    expected_result: List[int], values: List[int]
) -> None:
    array_binary_tree_generator = ArrayBinaryTreeGenerator()
    assert expected_result == array_binary_tree_generator.generate_tree(values=values)


def test_linked_list_binary_tree_build_success() -> None:
    def inorder_travser(output: List[Optional[int]], node: Node) -> None:
        if node.left:
            inorder_travser(output, node.left)
        output.append(node.value)
        if node.right:
            inorder_travser(output, node.right)

    linked_list_binary_tree = Node()
    node_values = [10, 21, 5, 9, 13, 28]
    for value in node_values:
        linked_list_binary_tree.insert(value)

    result: List[Optional[int]] = []
    expected_result = [5, 9, 10, 13, 21, 28]
    inorder_travser(result, linked_list_binary_tree)
    assert expected_result == result


def test_linked_list_binary_inorder_print_success() -> None:
    linked_list_binary_tree = Node()
    node_values = [53, 26, 60, 55, 40, 6, 35, 54, 58, 56]
    expected_result = [6, 26, 35, 40, 53, 54, 55, 56, 58, 60]
    for value in node_values:
        linked_list_binary_tree.insert(value)
    inorder_result = get_text_from_stdout(linked_list_binary_tree.inorder_print)
    assert expected_result == inorder_result


def test_linked_list_binary_preorder_print_success() -> None:
    linked_list_binary_tree = Node()
    node_values = [53, 26, 60, 55, 40, 6, 35, 54, 58, 56]
    expected_result = [53, 26, 6, 40, 35, 60, 55, 54, 58, 56]
    for value in node_values:
        linked_list_binary_tree.insert(value)
    preorder_result = get_text_from_stdout(linked_list_binary_tree.preorder_print)
    assert expected_result == preorder_result


def test_linked_list_binary_postorder_print_success() -> None:
    linked_list_binary_tree = Node()
    node_values = [53, 26, 60, 55, 40, 6, 35, 54, 58, 56]
    expected_result = [6, 35, 40, 26, 54, 56, 58, 55, 60, 53]
    for value in node_values:
        linked_list_binary_tree.insert(value)
    postorder_result = get_text_from_stdout(linked_list_binary_tree.postorder_print)
    assert expected_result == postorder_result


def test_linked_list_binary_search_success() -> None:
    linked_list_binary_tree = Node()
    node_values = [53, 26, 60, 55, 40, 6, 35, 54, 58, 56]
    expected_result = [
        [6, True],
        [10, False],
        [15, False],
        [0, False],
        [-1, False],
        [35, True],
    ]
    for value in node_values:
        linked_list_binary_tree.insert(value)

    for value, result in expected_result:
        assert result == linked_list_binary_tree.search(value)


def test_linked_list_binary_delete_success() -> None:
    linked_list_binary_tree = Node()
    node_values = [53, 26, 60, 55, 40, 6, 35, 54, 58, 56]
    ordered_node_values = sorted(node_values)
    for value in node_values:
        linked_list_binary_tree.insert(value)

    for value in node_values:
        # ignore the case of removing the root node
        if value == node_values[0]:
            continue

        root_node = deepcopy(linked_list_binary_tree)
        root_node.delete(value)
        inorder_result = get_text_from_stdout(root_node.inorder_print)
        expected_result = ordered_node_values.copy()
        expected_result.remove(value)
        assert inorder_result == expected_result
