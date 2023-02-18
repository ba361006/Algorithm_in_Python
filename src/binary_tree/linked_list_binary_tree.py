# -*- coding: utf-8 -*-
from __future__ import annotations

import os
import sys
from typing import Optional

sys.path.append(os.path.abspath("."))


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class LinkedListBinaryTree:
    def __init__(self, root: Optional[Node] = None) -> None:
        self.root = root

    def insert(self, node: Node) -> None:
        if self.root:
            self._recursive(base_node=self.root, incoming_node=node)
        else:
            self.root = node

    def _recursive(self, base_node: Node, incoming_node: Node) -> None:
        if incoming_node.value <= base_node.value:
            if base_node.left:
                self._recursive(base_node=base_node.left, incoming_node=incoming_node)
            else:
                base_node.left = incoming_node
        else:
            if base_node.right:
                self._recursive(base_node=base_node.right, incoming_node=incoming_node)
            else:
                base_node.right = incoming_node

    def inorder_print(self) -> None:
        if self.root is None:
            print("empty list")
            return
        self._inorder_print(self.root)

    def _inorder_print(self, node: Node) -> None:
        if node.left:
            self._inorder_print(node.left)
        print(node.value)
        if node.right:
            self._inorder_print(node.right)


if __name__ == "__main__":
    linked_list_b_tree = LinkedListBinaryTree()
    node_values = [10, 21, 5, 9, 13, 28]
    for data in node_values:
        linked_list_b_tree.insert(Node(data))
    linked_list_b_tree.inorder_print()
