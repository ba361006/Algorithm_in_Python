# -*- coding: utf-8 -*-
import os
import sys
from typing import Optional

sys.path.append(os.path.abspath("."))

from src.linked_list.resources import LinkedListBase


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList(LinkedListBase):
    head: Optional[Node]
    tail: Optional[Node]

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def add_node(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            # append to tail
            self.tail.next = node  # type: ignore
            node.previous = self.tail  # type: ignore
            self.tail = node

    def print_from_head(self) -> None:
        ptr = self.head
        while ptr:
            print(ptr.value)
            ptr = ptr.next

    def print_from_tail(self) -> None:
        ptr = self.tail
        while ptr:
            print(ptr.value)
            ptr = ptr.previous


if __name__ == "__main__":
    double_linked_list = DoubleLinkedList()
    double_linked_list.add_node(Node(1))
    double_linked_list.add_node(Node(2))
    double_linked_list.add_node(Node(3))

    double_linked_list.print_from_head()
    double_linked_list.print_from_tail()
