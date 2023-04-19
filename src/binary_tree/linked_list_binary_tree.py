# -*- coding: utf-8 -*-
from __future__ import annotations

import os
import sys
from typing import Optional

sys.path.append(os.path.abspath("."))


class Node:
    def __init__(self, value: Optional[int] = None) -> None:
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def insert(self, value) -> None:
        if self.value:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = Node(value)
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = Node(value)
        else:
            self.value = value


if __name__ == "__main__":
    node_values = [10, 21, 5, 9, 13, 28]
    linked_list_binary_tree = Node()
    for value in node_values:
        linked_list_binary_tree.insert(value)
        print(value)
