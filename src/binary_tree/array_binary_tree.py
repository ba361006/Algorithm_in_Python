# -*- coding: utf-8 -*-
import os
import sys
from typing import List

sys.path.append(os.path.abspath("."))


class ArrayBinaryTree:
    def generate_tree(self, empty_tree: List[int], values: List[int]) -> None:
        for node_value in values:
            index = 0

            # index would be the place to insert the node_value when get out the while loop
            while empty_tree[index]:
                if node_value < empty_tree[index]:
                    # go check left child node
                    index = 2 * index + 1
                else:
                    # go check right child node
                    index = 2 * index + 2

            empty_tree[index] = node_value
        self.tree = empty_tree


if __name__ == "__main__":
    binary_tree = ArrayBinaryTree()
    binary_tree.generate_tree(empty_tree=[0] * 7, values=[10, 21, 5, 9, 13, 28])
    print(binary_tree.tree)
