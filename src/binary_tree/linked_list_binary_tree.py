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

    def insert(self, value: int) -> None:
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

    def inorder_print(self) -> None:
        if self.left:
            self.left.inorder_print()
        print(self.value)
        if self.right:
            self.right.inorder_print()

    def preorder_print(self) -> None:
        print(self.value)
        if self.left:
            self.left.preorder_print()
        if self.right:
            self.right.preorder_print()

    def postorder_print(self) -> None:
        if self.left:
            self.left.postorder_print()
        if self.right:
            self.right.postorder_print()
        print(self.value)

    def search(self, value: int) -> bool:
        if self.value:
            if value == self.value:
                return True
            if value < self.value:
                if self.left:
                    return self.left.search(value)
            else:
                if self.right:
                    return self.right.search(value)
        return False


if __name__ == "__main__":
    node_values = [10, 21, 5, 9, 13, 28]
    linked_list_binary_tree = Node()

    # build the binary tree
    for node_value in node_values:
        linked_list_binary_tree.insert(node_value)

    # # Note:
    # # inorder: print in the middle
    # # preorder: print in the front
    # # post: print in the last
    # # inorder 中序, it will be printing from the minimum to the maximum
    # # LDR: Left(L) -> Root(D) -> Right(R)
    # linked_list_binary_tree.inorder_print()

    # # preorder 前序
    # # DLR: Root(D) -> Left(L) -> Right(R)
    # linked_list_binary_tree.preorder_print()

    # # postorder 後序
    # # LRD: Left(L) -> Right(R) -> Root(D)
    # linked_list_binary_tree.postorder_print()

    print(linked_list_binary_tree.search(-1))
