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

    def ending(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = node


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = linked_list.generate_nodes()
    linked_list.ending(Node(0))
    linked_list.print_list()
