# -*- coding: utf-8 -*-
import os
import sys
from copy import deepcopy
from typing import Callable
from typing import List
from typing import Optional

sys.path.append(os.path.abspath("."))

from tests.resource import BinaryTreeDataClass

from src.tree.array_binary_tree import ArrayBinaryTreeGenerator
from src.tree.linked_list_binary_tree import Node


def test_array_binary_tree_success_cases(
    array_binary_tree_samples: List[BinaryTreeDataClass],
) -> None:
    array_binary_tree_generator = ArrayBinaryTreeGenerator()
    for sample in array_binary_tree_samples:
        assert sample.array_result == array_binary_tree_generator.generate_tree(
            values=sample.values
        )


def test_linked_list_binary_tree_build_success(
    linked_list_binary_tree_samples: List[BinaryTreeDataClass],
) -> None:
    def inorder_travser(output: List[Optional[int]], node: Node) -> None:
        if node.left:
            inorder_travser(output, node.left)
        output.append(node.value)
        if node.right:
            inorder_travser(output, node.right)

    for sample in linked_list_binary_tree_samples:
        result: List[Optional[int]] = []
        root = Node()
        for value in sample.values:
            root.insert(value)
        inorder_travser(result, root)
        assert sample.inorder_result == result


def test_linked_list_binary_inorder_print_success(
    get_text_from_stdout: Callable[[Callable[[], None]], List[int]],
    linked_list_binary_tree_samples: List[BinaryTreeDataClass],
) -> None:
    for sample in linked_list_binary_tree_samples:
        root = Node()
        for value in sample.values:
            root.insert(value)
        inorder_result = get_text_from_stdout(root.inorder_print)
        assert sample.inorder_result == inorder_result


def test_linked_list_binary_preorder_print_success(
    get_text_from_stdout: Callable[[Callable[[], None]], List[int]],
    linked_list_binary_tree_samples: List[BinaryTreeDataClass],
) -> None:
    for sample in linked_list_binary_tree_samples:
        root = Node()
        for value in sample.values:
            root.insert(value)
        preorder_result = get_text_from_stdout(root.preorder_print)
        assert sample.preorder_result == preorder_result


def test_linked_list_binary_postorder_print_success(
    get_text_from_stdout: Callable[[Callable[[], None]], List[int]],
    linked_list_binary_tree_samples: List[BinaryTreeDataClass],
) -> None:
    for sample in linked_list_binary_tree_samples:
        root = Node()
        for value in sample.values:
            root.insert(value)
        postorder_result = get_text_from_stdout(root.postorder_print)
        assert sample.postorder_result == postorder_result


def test_linked_list_binary_search_success() -> None:
    root = Node()
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
        root.insert(value)

    for value, result in expected_result:
        assert result == root.search(value)


def test_linked_list_binary_delete_success(
    get_text_from_stdout: Callable[[Callable[[], None]], List[int]],
    linked_list_binary_tree_samples: List[BinaryTreeDataClass],
) -> None:
    for sample in linked_list_binary_tree_samples:
        root = Node()
        ordered_node_values = sorted(sample.values)
        for value in sample.values:
            root.insert(value)

        for value in sample.values:
            # ignore the case of removing the root node
            if value == sample.values[0]:
                continue

            root_node = deepcopy(root)
            root_node.delete(value)
            inorder_result = get_text_from_stdout(root_node.inorder_print)
            expected_result = ordered_node_values.copy()
            expected_result.remove(value)
            assert inorder_result == expected_result
