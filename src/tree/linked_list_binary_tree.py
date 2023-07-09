# -*- coding: utf-8 -*-
from __future__ import annotations

import os
import sys
from typing import List
from typing import Optional

sys.path.append(os.path.abspath("."))

# pylint: disable=line-too-long
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

    def delete(self, value: int) -> None:
        # pylint: disable=too-many-branches
        if self.value is None:
            return

        # get the previous node and target node(the node to be deleted)
        direction = ""
        previous_node = None
        current_node = self
        while True:
            if value < current_node.value:  # type: ignore
                if current_node.left:
                    direction = "left"
                    previous_node = current_node
                    current_node = current_node.left
                else:
                    return
            elif value > current_node.value:  # type: ignore
                if current_node.right:
                    direction = "right"
                    previous_node = current_node
                    current_node = current_node.right
                else:
                    return
            else:
                break

        if current_node.left:
            # target node has left subtree, we are going to replace the target node
            # with the largest node from the subtree
            subtree_previous_node = current_node
            subtree_root_node = current_node.left
            subtree_current_node = current_node.left

            if subtree_root_node.right is None:
                # root of the subtree node is the largest node
                subtree_root_node.right = current_node.right
                setattr(previous_node, direction, subtree_root_node)
            else:
                # find the largest node
                while subtree_current_node.right:
                    subtree_previous_node = subtree_current_node
                    subtree_current_node = subtree_current_node.right

                # handle the case that the largest node has a left node
                subtree_previous_node.right = subtree_current_node.left

                # replace the target node with the largest node from subtree
                subtree_current_node.left = current_node.left
                subtree_current_node.right = current_node.right
                setattr(previous_node, direction, subtree_current_node)

        elif current_node.right:
            # has right subtree, replace current_node with the right child node
            setattr(previous_node, direction, current_node.right)
        else:
            # leaf node, set previous_node's left / right child node to None
            setattr(previous_node, direction, None)


def return_inorder_value(node: Optional[Node]) -> List[int]:
    # for a leaf node, it would be:
    # [] + [node.value] + []

    # for a node with left, it would be:
    # ([]+[left_child.value]+[]) + [node.value] + []

    # for a node with both left and right,  it would be:
    # ([]+[left_child.value]+[]) + [node.value] + ([]+[right_child.value]+[])
    if node is None:
        return []
    return return_inorder_value(node.left) + [node.value] + return_inorder_value(node.right)  # type: ignore


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

    # # search
    # print(linked_list_binary_tree.search(-1))

    # # delete
    # linked_list_binary_tree.inorder_print()
    # linked_list_binary_tree.delete(10)
    # print("#" * 20)
    # linked_list_binary_tree.inorder_print()

    # return inorder list value
    print(return_inorder_value(linked_list_binary_tree))
