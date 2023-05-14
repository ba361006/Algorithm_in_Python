# -*- coding: utf-8 -*-
import os
import sys
from typing import List
from typing import Tuple

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

    def min_heap_pop(self) -> Tuple[int, List[int]]:
        tree = self.build_min_heapify()
        poped_value = tree.pop(0)
        self.base = [tree.pop()] + tree
        return (poped_value, self.build_min_heapify())

    def max_heap_pop(self) -> Tuple[int, List[int]]:
        tree = self.build_max_heapify()
        poped_value = tree.pop(0)
        self.base = [tree.pop()] + tree
        return (poped_value, self.build_max_heapify())

    def min_push_pop(self, value: int) -> Tuple[int, List[int]]:
        poped_value, tree = self.min_heap_pop()
        self.base = tree
        return (poped_value, self.min_heap_push(value))

    def max_push_pop(self, value: int) -> Tuple[int, List[int]]:
        poped_value, tree = self.max_heap_pop()
        self.base = tree
        return (poped_value, self.max_heap_push(value))

    def get_n_min(self, value: int) -> List[int]:
        ori_base = self.base.copy()
        result = []
        for _ in range(value):
            poped_value, _ = self.min_heap_pop()
            result.append(poped_value)
        self.base = ori_base
        return result

    def get_n_max(self, value: int) -> List[int]:
        ori_base = self.base.copy()
        result = []
        for _ in range(value):
            poped_value, _ = self.max_heap_pop()
            result.append(poped_value)
        self.base = ori_base
        return result

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

    # # build heap tree
    # min_heap_tree = array_heap_tree.build_min_heapify()
    # max_heap_tree = array_heap_tree.build_max_heapify()
    # print("min_heap_tree: ", min_heap_tree)
    # print("max_heap_tree: ", max_heap_tree)

    # push and pop
    # print(array_heap_tree.min_heap_push(25))
    # print(array_heap_tree.max_heap_push(27))
    # print(array_heap_tree.min_heap_pop())
    # print(array_heap_tree.max_heap_pop())
    # print(array_heap_tree.min_push_pop(11))
    # print(array_heap_tree.max_push_pop(11))

    # # get n min / max
    # print(array_heap_tree.get_n_min(3))
    # print(array_heap_tree.base)
    # print(array_heap_tree.get_n_max(3))
    # print(array_heap_tree.base)
