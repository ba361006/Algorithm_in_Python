# -*- coding: utf-8 -*-
from __future__ import annotations

import os
import sys

sys.path.append(os.path.abspath("."))

from typing import List


class CocktailSort:
    def __init__(self) -> None:
        pass

    def sort(self, int_list: List[int]) -> List[int]:
        length = len(int_list)
        anchor = 0

        while anchor != length // 2:
            for i in range(anchor, length - 1 - anchor):
                if int_list[i] > int_list[i + 1]:
                    int_list[i], int_list[i + 1] = int_list[i + 1], int_list[i]
            anchor += 1
            for i in range(length - 1 - anchor, anchor - 1, -1):
                if int_list[i] < int_list[i - 1]:
                    int_list[i], int_list[i - 1] = int_list[i - 1], int_list[i]
        return int_list


if __name__ == "__main__":
    values = [6, 1, 5, 7, 3]
    solution = CocktailSort()
    print(solution.sort(values))
