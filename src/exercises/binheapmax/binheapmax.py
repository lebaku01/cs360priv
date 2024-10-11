#!/usr/bin/env python3
"""
Binary Heap implementation

@authors:
@version: 2022.9
"""

from typing import Any


class BinaryHeapMax:
    """Heap class implementation"""

    def __init__(self) -> None:
        """Initializer"""
        self._heap: list[Any] = []
        self._size = 0

    def _perc_up(self, cur_idx: int) -> None:
        """Move a node up"""
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._heap[cur_idx] > self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[cur_idx],
                )
            cur_idx = parent_idx

    def _perc_down(self, cur_idx: int) -> None:
        """Move a node down"""
        while 2 * cur_idx + 1 < len(self._heap):
            max_child_idx = self._get_max_child(cur_idx)
            if self._heap[cur_idx] < self._heap[max_child_idx]:
                self._heap[cur_idx], self._heap[max_child_idx] = (
                    self._heap[max_child_idx],
                    self._heap[cur_idx],
                )
            else:
                return
            cur_idx = max_child_idx

    def add(self, item: Any) -> None:
        """Add a new item to the heap"""
        self._heap.append(item)
        self._perc_up(len(self._heap) - 1)

    def remove(self) -> Any:
        """Remove an item from the heap"""
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._perc_down(0)
        return result

    def heapify(self, not_a_heap: list) -> None:
        """Turn a list into a heap"""
        self._heap = not_a_heap[:]
        cur_idx = len(self._heap) // 2 - 1
        while cur_idx >= 0:
            self._perc_down(cur_idx)
            cur_idx = cur_idx - 1

    def _get_max_child(self, parent_idx: int) -> int:
        """Get index of the greater child"""
        if 2 * parent_idx + 2 > len(self._heap) - 1:
            return 2 * parent_idx + 1
        if self._heap[2 * parent_idx + 1] > self._heap[2 * parent_idx + 2]:
            return 2 * parent_idx + 1
        return 2 * parent_idx + 2

    def __len__(self) -> int:
        """Get heap size"""
        return self._size

    def __str__(self) -> str:
        """Heap as a string """
        return str(self._heap)

#test
#a = BinaryHeapMax()
#a.heapify([1, 2, 3, 4, 5, 6, 7, 8, 9])
#for i in range(9):
#    a.add(i)
#for i in range(9):
#    print(a.remove())
