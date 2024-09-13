#!/usr/bin/env python3
"""
`stack` implementation

@authors: Roman Yasinovskyy
@version: 2021.11
"""

import heapq
from typing import Any



class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


class Stack:
    """
    LIFO data structure

    Items are added and removed at the same end of the collection
    """

    def __init__(self):
        """Initialize a stack using heapq"""
        # NOTE: Do not modify this method
        self.items = []

    def push(self, item: Any) -> None:
        """
        Add a new item to stack

        :param item: a new item to push onto the stack
        """
        #
        # check if the stack is empty before calling the peek method in case #1
        #
        if len(self.items) != 0:
            #
            # push item and make its priority one
            # less than the current top of the stack
            #
            heapq.heappush(self.items, (self.__peek()[0] - 1, item))
        else:
            heapq.heappush(self.items, (0, item))

    def pop(self) -> Any:
        """
        Remove an item from the stack

        :return: the top element of the stack
        :raise StackError if the stack is empty
        """
        if len(self.items) == 0:
            raise StackError()
        else:
            return heapq.heappop(self.items)[1]

    def peek(self) -> Any:
        """
        Look at the top item without removing it

        :return: the top element of the stack
        :raise StackError if the stack is empty
        """
        popped = heapq.heappop(self.items)
        heapq.heappush(self.items, popped)
        return popped[1]

    def __peek(self):
        """
        A private version of the peek method that returns the top element of the heap as a tuple, rather than as
        a single element
        :return: the top tuple of the heap
        :raise StackError if the stack is empty

        """
        popped = heapq.heappop(self.items)
        heapq.heappush(self.items, popped)
        return popped

    def __bool__(self) -> bool:
        """
        Evaluate the stack

        :return: False if the stack is empty, True otherwise
        """
        return len(self.items) > 0

    def __len__(self) -> int:
        """
        Return the number of items in the stack

        :return: number of items in the stack (0 if the stack is empty)
        """
        #
        #    recursively take apart the stack, and then when the stack is empty put the
        #    stack back together while counting the number of calls to count() on the way
        #    out
        #
        def count(length: int) -> int:
            if not self.__bool__():
                return 0
            else:
                popped = heapq.heappop(self.items)
                depth = count(length + 1)
                heapq.heappush(self.items, popped)
                return depth + 1

        return count(0)

# really basic main



