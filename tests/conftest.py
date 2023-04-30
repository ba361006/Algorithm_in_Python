# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.abspath("."))

import io
import pytest
from typing import List
from typing import Callable
from tests.resource import BinaryTreeDataClass


@pytest.fixture
def get_text_from_stdout() -> Callable[[Callable[[], None]], List[int]]:
    def _get_text_from_stdout(printing_function: Callable[[], None]) -> List[int]:
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

    return _get_text_from_stdout


@pytest.fixture(name="array_binary_tree_samples")
def array_binary_tree_samples() -> List[BinaryTreeDataClass]:
    return [
        BinaryTreeDataClass(
            values=[10, 21, 5, 9, 13, 28], array_result=[10, 5, 21, 0, 9, 13, 28]
        ),
        BinaryTreeDataClass(
            values=[53, 26, 60, 55, 40, 6, 35, 54, 58, 56],
            array_result=[
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
        ),
    ]


@pytest.fixture(name="linked_list_binary_tree_samples")
def linked_list_binary_tree_samples() -> List[BinaryTreeDataClass]:
    return [
        BinaryTreeDataClass(
            values=[10, 21, 5, 9, 13, 28],
            inorder_result=[5, 9, 10, 13, 21, 28],
            preorder_result=[10, 5, 9, 21, 13, 28],
            postorder_result=[9, 5, 13, 28, 21, 10],
        ),
        BinaryTreeDataClass(
            values=[53, 26, 60, 55, 40, 6, 35, 54, 58, 56],
            inorder_result=[6, 26, 35, 40, 53, 54, 55, 56, 58, 60],
            preorder_result=[53, 26, 6, 40, 35, 60, 55, 54, 58, 56],
            postorder_result=[6, 35, 40, 26, 54, 56, 58, 55, 60, 53],
        ),
    ]
