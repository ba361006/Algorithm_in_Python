# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.abspath("."))

from src.chap_3 import resources
from src.chap_3 import task_3_8_3
from src.chap_3 import task_3_8_4
from src.chap_3 import task_3_8_5


def test_task_3_8_3():
    solution = task_3_8_3.Solution()
    solution.start_task(resources.Node(123))
