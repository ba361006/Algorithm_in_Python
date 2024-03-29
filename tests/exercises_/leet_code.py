# -*- coding: utf-8 -*-
from typing import List
from typing import Optional


class Node:
    def __init__(self, value: Optional[int] = None) -> None:
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class Solution1382:
    """
    1382, Balance a Binary Search Tree
    Given the root of a binary search tree, return a balanced binary search tree
    with the same node values.
    If there is more than one answer, return any of them.
    A binary search tree is balanced if the depth of the two subtrees of every node
    never differs by more than 1.
    """

    def balance_bst(self, root: Node) -> Optional[Node]:
        def build_bst(
            left: int, right: int, array: List[Optional[int]]
        ) -> Optional[Node]:
            if left > right:
                return None
            mid = (right + left) // 2
            root = Node(array[mid])
            root.left = build_bst(left, mid - 1, array)
            root.right = build_bst(mid + 1, right, array)
            return root

        def recursive(node: Optional[Node]) -> List[Optional[int]]:
            if node is None:
                return []
            return recursive(node.left) + [node.value] + recursive(node.right)

        array = recursive(root)
        return build_bst(0, len(array) - 1, array)
