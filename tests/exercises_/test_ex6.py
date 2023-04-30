# -*- coding: utf-8 -*-
import io
import os
import sys
from copy import deepcopy

sys.path.append(os.path.abspath("."))

from typing import Callable
from typing import List
from tests.resource import BinaryTreeDataClass
from src.exercises.ex6 import Node
from src.exercises.ex6 import Exercise61
from src.exercises.ex6 import Exercise62
from src.exercises.ex6 import Exercise63


def test_ex6_data_structure_success(
    get_text_from_stdout: Callable[[Callable[[], None]], List[int]],
    linked_list_binary_tree_samples: List[BinaryTreeDataClass],
) -> None:
    for sample in linked_list_binary_tree_samples:
        root = Node()
        for value in sample.values:
            root.insert(value)

        assert sample.preorder_result == get_text_from_stdout(
            lambda: root.preorder_print(0)  # type: ignore # pylint: disable=cell-var-from-loop
        )
        assert sample.postorder_result == get_text_from_stdout(root.postorder_print)

        # delete test
        for value in sample.values:
            expected_result = sample.values.copy()
            expected_result.remove(value)
            copy_root = deepcopy(root)
            deleted_root = copy_root.delete(value)
            raw_result = get_text_from_stdout(deleted_root.postorder_print)
            sorted_result = sorted(list(map(int, raw_result)))
            assert sorted(expected_result) == sorted_result


def test_ex6_1_solution_success(
    get_text_from_stdout: Callable[[Callable[[], None]], List[int]],
) -> None:
    ex6_1 = Exercise61()
    preorder_result = get_text_from_stdout(ex6_1.solution)

    # ignore annoying printing
    original_stdout = sys.stdout
    output = io.StringIO()
    sys.stdout = output
    amount_of_leaf_nodes = ex6_1.solution()
    sys.stdout = original_stdout

    expected_result = [10, 5, 3, 1, 4, 9, 21, 13, 17, 28, 32]
    assert expected_result == preorder_result
    assert amount_of_leaf_nodes == 5


def test_ex6_2_solution_success(
    get_text_from_stdout: Callable[[Callable[[], None]], List[int]],
) -> None:
    ex6_2 = Exercise62()

    # ignore annoying printing
    original_stdout = sys.stdout
    output = io.StringIO()
    sys.stdout = output
    depth = ex6_2.solution()
    sys.stdout = original_stdout

    expected_result = [1, 4, 3, 9, 5, 17, 13, 32, 28, 21, 10]
    postorder_result = get_text_from_stdout(
        lambda: ex6_2.solution()  # type:ignore # pylint: disable=unnecessary-lambda
    )
    assert expected_result == postorder_result
    assert depth == 4


def test_ex6_3_solution_success(
    get_text_from_stdout: Callable[[Callable[[], None]], List[int]],
) -> None:
    ex6_3 = Exercise63()
    deleted_result = get_text_from_stdout(ex6_3.solution)
    expected_result = [1, 4, 3, 9, 5, 17, 32, 28, 21, 13]
    assert expected_result == deleted_result
