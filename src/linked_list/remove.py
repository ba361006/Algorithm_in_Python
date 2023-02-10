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

    def remove(self, remove_value: int) -> None:
        if self.head is None:
            raise ValueError("there is no node in this linkedlist")
        if self.head.value == remove_value:
            self.head = self.head.next
            return

        # traverse until next node is the wanted node
        ptr = self.head
        while ptr.next:
            if ptr.next.value == remove_value:
                break
            ptr = ptr.next

        if ptr.next:
            ptr.next = ptr.next.next
        else:
            raise ValueError(f"{remove_value} not in the linked_list")


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = linked_list.generate_nodes()
    linked_list.remove(1)
    linked_list.print_list()
