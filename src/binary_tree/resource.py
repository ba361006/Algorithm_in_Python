# -*- coding: utf-8 -*-
import math
import os
import sys
from typing import List

sys.path.append(os.path.abspath("."))


class ArrayBinaryTree:
    def __init__(self) -> None:
        self.tree: List[int] = []

    def generate_tree(self, values: List[int]) -> None:
        node_amount = len(values)
        tree = self._generate_empty_tree(node_amount)
        for node_value in values:
            index = 0

            # index would be the place to insert the node_value when get out the while loop
            while tree[index]:
                if node_value < tree[index]:
                    # go check left child node
                    index = 2 * index + 1
                else:
                    # go check right child node
                    index = 2 * index + 2

            tree[index] = node_value
        self.tree = tree

    def _generate_empty_tree(self, node_amount: int) -> List[int]:
        """
        ex: we at lease need a 3 layers binary_tree if the given node_amount is 6
        min_layer = ceil(log2(node_amount+1))
        maximum_node_of_the_min_layer = 2**min_layer - 1
        """
        min_layer = math.ceil(math.log2(node_amount + 1))
        return [0] * (2**min_layer - 1)


if __name__ == "__main__":
    binary_tree = ArrayBinaryTree()
    binary_tree.generate_tree([10, 21, 5, 9, 13, 28])
    expected_result = [10, 5, 21, 0, 9, 13, 28]
    assert expected_result == binary_tree.tree
