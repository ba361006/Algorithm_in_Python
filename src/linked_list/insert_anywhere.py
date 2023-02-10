# -*- coding: utf-8 -*-
import os
import sys
from typing import Optional

sys.path.append(os.path.abspath("."))

from src.linked_list.resources import LinkedListBase
from src.linked_list.resources import Node


class LinkedList(LinkedListBase):
    # this is to solve mypy's error -> cannot determine type of head
    head: Optional[Node]

    def insert(self, index: int, node: Node) -> None:
        # if index equals to zero, just let the incoming node become head
        # and let it point to the original head
        if index == 0:
            node.next = self.head
            self.head = node
            return

        # traverse and stop at just before the wanted node
        count = 1
        ptr = self.head
        while ptr.next:
            if count == index:
                break
            ptr = ptr.next
            count += 1

        # the count should equal to index if the index is in the range
        # otherwise raise an exception
        if count != index:
            raise IndexError(
                f"Index out of range, we got {count} node but given index is {index}"
            )

        # append the node
        node.next = ptr.next
        ptr.next = node


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = linked_list.generate_nodes()
    linked_list.insert(index=0, node=Node(100))
    linked_list.print_list()
