# -*- coding: utf-8 -*-
import os
import sys

import pytest

sys.path.append(os.path.abspath("."))

from typing import List
from typing import Optional
from typing import Any
from src.sorting.bubble_sort import BubbleSort
from src.sorting.cocktail_sort import CocktailSort


@pytest.fixture
def setup_data() -> List[Optional[List[int]]]:
    return [
        [5, 4, 3, 2, 1],
        [1, 5, 6, 7, 3],
        [0],
        [],
        [1, 2, 3, 4, 5],
        [12, 9, 8, 135, 7, 1, 9668, 2, 7, 8, 1, 3],
    ]


def test_bubble_sort(setup_data: Any) -> None:
    solution = BubbleSort()
    for data in setup_data:
        assert solution.sort(data) == sorted(data)


def test_cocktail_sort(setup_data: Any) -> None:
    solution = CocktailSort()
    for data in setup_data:
        assert solution.sort(data) == sorted(data)
