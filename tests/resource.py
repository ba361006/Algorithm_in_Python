# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import List
from typing import Optional


@dataclass
class BinaryTreeDataClass:
    values: List[int]
    array_result: Optional[List[int]] = None
    inorder_result: Optional[List[int]] = None
    preorder_result: Optional[List[int]] = None
    postorder_result: Optional[List[int]] = None
