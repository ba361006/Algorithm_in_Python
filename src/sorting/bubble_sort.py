# -*- coding: utf-8 -*-
from __future__ import annotations

import os
import sys

sys.path.append(os.path.abspath("."))

from typing import List


class BubbleSort:
    def __init__(self) -> None:
        pass

    def sort(self, int_list: List[int]) -> List[int]:
        length = len(int_list)
        # bubble sort will put the maximum number to the end in every outter loop(the i loop)
        # so the inspection location can decrease based on the number of iterations.
        for i in range(length - 1):
            for j in range(length - 1 - i):
                if int_list[j] > int_list[j + 1]:
                    int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
        return int_list


if __name__ == "__main__":
    values = [6, 1, 5, 7, 3]
    solution = BubbleSort()
    print(solution.sort(int_list=values))
