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

    def begining(self, node: Node) -> None:
        node.next = self.head
        self.head = node


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = linked_list.generate_nodes()
    linked_list.begining(Node(0))
    linked_list.print_list()
