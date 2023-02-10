# -*- coding: utf-8 -*-
import os
import sys
from typing import List

import pytest

sys.path.append(os.path.abspath("."))

from src.linked_list.resources import Node, traverse_linked_list
from src.linked_list import insert_to_head
from src.linked_list import insert_to_tail
from src.linked_list import insert_anywhere


def test_insert_to_head_success() -> None:
    expected_result = [100, 1, 2, 3]
    linked_list = insert_to_head.LinkedList()
    linked_list.head = linked_list.generate_nodes()
    linked_list.begining(Node(100))
    assert traverse_linked_list(linked_list) == expected_result


def test_insert_to_tail_success() -> None:
    expected_result = [1, 2, 3, 100]
    linked_list = insert_to_tail.LinkedList()
    linked_list.head = linked_list.generate_nodes()
    linked_list.ending(Node(100))
    assert traverse_linked_list(linked_list) == expected_result


@pytest.mark.parametrize(
    "expected_result, index, node_value",
    [
        ([100, 1, 2, 3], 0, 100),
        ([1, 100, 2, 3], 1, 100),
        ([1, 2, 100, 3], 2, 100),
        ([1, 2, 3, 100], 3, 100),
    ],
)
def test_insert_anywhere_insert_success_cases(
    expected_result: List[int], index: int, node_value: int
) -> None:
    linked_list = insert_anywhere.LinkedList()
    linked_list.head = linked_list.generate_nodes()
    linked_list.insert(index, Node(node_value))
    assert traverse_linked_list(linked_list) == expected_result


def test_insert_anywhere_insert_index_out_of_range_should_fail() -> None:
    linked_list = insert_anywhere.LinkedList()
    linked_list.head = linked_list.generate_nodes()
    with pytest.raises(IndexError):
        linked_list.insert(100, Node(10))
