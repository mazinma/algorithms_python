#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = 'key', 'value'

        def __init__(self, k, v):
            self.key = k
            self.value = v

        def __lt__(self, other):
            return self.key < other.key

    def is_empty(self):
        """Return True if the priority queue is empty."""
        return len(self) == 0


class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap."""

    # --------------------- nonpublic behaviors --------------------
    @staticmethod
    def _parent(j):
        return (j - 1) // 2

    @staticmethod
    def _left(j):
        return 2 * j + 1

    @staticmethod
    def _right(j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _up_heap(self, j):
        parent = self._parent(j)

        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._up_heap(parent)

    def _down_heap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left

            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right

            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._down_heap(small_child)

    # --------------------- public behaviors --------------------
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = []

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))
        self._up_heap(len(self._data) - 1)

    def min(self):
        """Return but do not remove (k, v) tuple with minimum key."""
        if self.is_empty():
            raise Exception('Priority queue is empty.')

        item = self._data[0]

        return item.key, item.value

    def remove_min(self):
        """Remove and return (k, v) tuple with minimum key."""
        if self.is_empty():
            raise Exception('Priority queue is empty.')

        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._down_heap(0)

        return item.key, item.value
