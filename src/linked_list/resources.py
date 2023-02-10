# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import List
from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional[Node] = None) -> None:
        self.value = value
        self.next = next


class LinkedListBase:
    def __init__(self, node: Optional[Node] = None) -> None:
        self.head: Optional[Node] = node

    def print_list(self) -> None:
        ptr = self.head
        while ptr:
            print(ptr.value)
            ptr = ptr.next

    def generate_nodes(self) -> Node:
        n3 = Node(3)
        n2 = Node(2, n3)
        n1 = Node(1, n2)
        return n1


def traverse_linked_list(linked_list: LinkedListBase) -> List[int]:
    result = []
    pointer = linked_list.head
    while pointer:
        result.append(pointer.value)
        pointer = pointer.next
    return result
