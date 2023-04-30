# -*- coding: utf-8 -*-
from __future__ import annotations

import os
import sys

sys.path.append(os.path.abspath("."))

from typing import List, Optional


class Node:
    def __init__(self, value: Optional[int] = None) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: int) -> None:
        if self.value is None:
            self.value = value
            return

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

    def preorder_print(self, amount_of_leaf_node: int) -> int:
        print(self.value)
        if self.left:
            amount_of_leaf_node = self.left.preorder_print(amount_of_leaf_node)
        if self.right:
            amount_of_leaf_node = self.right.preorder_print(amount_of_leaf_node)
        if self.left is None and self.right is None:
            amount_of_leaf_node += 1
        return amount_of_leaf_node

    def postorder_print(self) -> None:
        if self.left:
            self.left.postorder_print()
        if self.right:
            self.right.postorder_print()
        print(self.value)

    def get_depth(self) -> int:
        maximum_depth = 1
        stack = [(self, maximum_depth)]
        while stack:
            node, depth = stack.pop()
            maximum_depth = max(depth, maximum_depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return maximum_depth

    def delete(self, value: int) -> Node:
        if self.value is None:
            return

        direction = ""
        previous_node = self
        current_node = self

        # find the target node(the node to be deleted)
        while value != current_node.value:
            if value < current_node.value:
                if current_node.left:
                    previous_node = current_node
                    current_node = current_node.left
                    direction = "left"
                else:
                    return self
            elif value > current_node.value:
                if current_node.right:
                    previous_node = current_node
                    current_node = current_node.right
                    direction = "right"
                else:
                    return self

        if previous_node == current_node:
            new_root: Node
            # target node is root node
            if current_node.right:
                # 1. pop minimum node
                minimum_node = self.__pop_minimum_node(root=current_node.right)

                # 2. the minimum node points to the current_node's left and right
                minimum_node.left = current_node.left
                if minimum_node != current_node.right:
                    # handle the case that the root of right subtree is the minimumn node
                    minimum_node.right = current_node.right
                new_root = minimum_node
            elif current_node.left:
                new_root = self.left
            else:
                # should never go here
                raise ValueError("Try to remove root")
            return new_root

        if current_node.right:
            # 1. pop the minimum node
            minimum_node = self.__pop_minimum_node(root=current_node.right)

            # 2. the minimum node points to the target node(current_node)'s left and right
            minimum_node.left = current_node.left
            if minimum_node != current_node.right:
                # handle the case that the root of right subtree is the minimumn node
                minimum_node.right = current_node.right

            # 3. previous_node points to the minimum node
            setattr(previous_node, direction, minimum_node)
        elif current_node.left:
            # 1. previous_node points to the target node's left
            setattr(previous_node, direction, current_node.left)
        else:
            setattr(previous_node, direction, None)
        return self

    def __pop_minimum_node(self, root: Node) -> Node:
        previous_node = root
        current_node = root

        # find the minimumn node
        while current_node.left:
            if current_node.left:
                previous_node = current_node
            current_node = current_node.left

        # the root is the minimum node, pop the root and return its right node
        if previous_node == current_node:
            return current_node

        # handle the case if the minimum node has right sub node
        previous_node.left = current_node.right
        return current_node


class Exercise6_1:
    def __init__(
        self, values: List[int] = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]
    ) -> None:
        # 1. preorder print
        # 2. count the amount of leaf nodes
        self.values = values

    def solution(self) -> int:
        root = Node()
        for value in self.values:
            root.insert(value)
        amount_of_leaf_node = root.preorder_print(amount_of_leaf_node=0)
        return amount_of_leaf_node


class Exercise6_2:
    def __init__(
        self, values: List[int] = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]
    ) -> None:
        # 1. postorder print
        # 2. count the levels / depth of tree
        self.values = values

    def solution(self) -> int:
        root = Node()
        for value in self.values:
            root.insert(value)
        root.postorder_print()
        return root.get_depth()


class Exercise6_3:
    def __init__(
        self, values: List[int] = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]
    ) -> None:
        # 1. replace the deleted node with the  minimum node from the right subtree
        # 2. postorder print
        self.values = values

    def solution(self) -> None:
        root = Node()
        for value in self.values:
            root.insert(value)
        root = root.delete(10)
        root.postorder_print()


import os
import sys
import io
from typing import List
from typing import Callable


def get_text_from_stdout(printing_function: Callable[[], None]) -> List[int]:
    # Save the current stdout stream
    original_stdout = sys.stdout

    # Create a new stream to capture the output
    output = io.StringIO()
    sys.stdout = output

    # Call the function that prints some text
    printing_function()

    # Reset the stdout stream
    sys.stdout = original_stdout

    # Get the printed text as a string
    raw_text = output.getvalue()

    return list(map(int, raw_text.split()))


if __name__ == "__main__":
    Ex61 = Exercise6_1()
    print(f"The amount of leaf node: {Ex61.solution()}")
    print("#" * 20)

    Ex62 = Exercise6_2()
    print(f"The depth of binary tree: {Ex62.solution()}")
    print("#" * 20)

    Ex63 = Exercise6_3()
    Ex63.solution()
