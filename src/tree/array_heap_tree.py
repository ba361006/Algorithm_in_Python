# -*- coding: utf-8 -*-
import os
import sys
from typing import List

sys.path.append(os.path.abspath("."))


class ArrayHeapTree:
    def __init__(self, values: List[int]) -> None:
        self.base = values

    def build_min_heapify(self) -> List[int]:
        if not self.base:
            return self.base
        tree = self.base.copy()
        subnodes_indices = self.__get_subnodes_indices(tree)
        subnodes_table = subnodes_indices.copy()

        while subnodes_indices:
            node_index = subnodes_indices.pop()

            # get child nodes
            left_child = tree[2 * node_index + 1]
            right_child = float("inf")
            if (2 * node_index + 2) < len(tree):
                right_child = tree[2 * node_index + 2]

            if tree[node_index] > min(left_child, right_child):
                if left_child <= right_child:
                    tree[node_index], tree[2 * node_index + 1] = (
                        tree[2 * node_index + 1],
                        tree[node_index],
                    )
                    # subnodes_table indicates that the node has subnode(s)
                    # even it's swapped, the node at this position must still have subnode(s)
                    if 2 * node_index + 1 in subnodes_table:
                        subnodes_indices.append(2 * node_index + 1)
                else:
                    tree[node_index], tree[2 * node_index + 2] = (
                        tree[2 * node_index + 2],
                        tree[node_index],
                    )
                    if 2 * node_index + 2 in subnodes_table:
                        subnodes_indices.append(2 * node_index + 2)
        return tree

    def build_max_heapify(self) -> List[int]:
        if not self.base:
            return self.base
        tree = self.base.copy()
        subnodes_indices = self.__get_subnodes_indices(tree)
        subnodes_table = subnodes_indices.copy()

        while subnodes_indices:
            node_index = subnodes_indices.pop()

            # get child nodes, we assume the minimum node number is 0
            left_child = tree[2 * node_index + 1]
            right_child = -1
            if (2 * node_index + 2) < len(tree):
                right_child = tree[2 * node_index + 2]

            if tree[node_index] < max(left_child, right_child):
                if left_child >= right_child:
                    tree[node_index], tree[2 * node_index + 1] = (
                        tree[2 * node_index + 1],
                        tree[node_index],
                    )
                    # subnodes_table indicates that the node has subnode(s)
                    # even it's swapped, the node at this position must still have subnode(s)
                    if 2 * node_index + 1 in subnodes_table:
                        subnodes_indices.append(2 * node_index + 1)
                else:
                    tree[node_index], tree[2 * node_index + 2] = (
                        tree[2 * node_index + 2],
                        tree[node_index],
                    )
                    if 2 * node_index + 2 in subnodes_table:
                        subnodes_indices.append(2 * node_index + 2)
        return tree

    def min_heap_push(self, value: int) -> List[int]:
        self.base.append(value)
        return self.build_min_heapify()

    def max_heap_push(self, value: int) -> List[int]:
        self.base.append(value)
        return self.build_max_heapify()

    def __get_subnodes_indices(self, tree: List[int]) -> List[int]:
        result = []
        index = 0
        while (2 * index + 1) < len(tree):
            result.append(index)
            index += 1
        return result


if __name__ == "__main__":
    example = [10, 21, 5, 9, 13, 28, 3]
    array_heap_tree = ArrayHeapTree(example)
    print(array_heap_tree.base)

    # # build heap tree
    # min_heap_tree = array_heap_tree.build_min_heapify()
    # max_heap_tree = array_heap_tree.build_max_heapify()
    # print("min_heap_tree: ", min_heap_tree)
    # print("max_heap_tree: ", max_heap_tree)

    # push and pop
    # print(array_heap_tree.min_heap_push(25))
    # print(array_heap_tree.max_heap_push(27))
