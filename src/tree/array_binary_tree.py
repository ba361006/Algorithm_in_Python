# -*- coding: utf-8 -*-
import os
import sys
from typing import Dict
from typing import List

sys.path.append(os.path.abspath("."))


class ArrayBinaryTreeGenerator:
    # I didn't handle the case of the same node values
    def generate_tree(self, values: List[int]) -> List[int]:
        if not values:
            return []

        # {node_index: node_value}
        nodes_mapper: Dict[int, int] = {}

        for value in values:
            index = 0
            # get index of the node
            while index in nodes_mapper:
                if value < nodes_mapper[index]:
                    # go check left child node
                    index = 2 * index + 1
                else:
                    # go check right child node
                    index = 2 * index + 2
            nodes_mapper[index] = value

        # take the maximum index as the length of array
        binary_tree = [0] * (1 + max(nodes_mapper.keys()))
        for node_index, node_value in nodes_mapper.items():
            binary_tree[node_index] = node_value
        return binary_tree


if __name__ == "__main__":
    binary_tree_generator = ArrayBinaryTreeGenerator()
    print(binary_tree_generator.generate_tree(values=[10, 8, 13]))
