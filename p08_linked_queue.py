#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


class Queue:
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = 'element', 'next'

        def __init__(self, elm, nxt):
            self.element = elm
            self.next = nxt

    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0                # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue if empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the elements at the front of the queue."""
        if self.is_empty():
            return

        return self._head.element     # from aligned with head of list

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO)."""
        if self.is_empty():
            return

        answer = self._head.element
        self._head = self._head.next
        self._size -= 1

        if self.is_empty():           # special case as queue is empty
            self._tail = None         # removed head had been the tail

        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)  # node will be new tail node

        if self.is_empty():
            self._head = newest       # special case: previously empty
        else:
            self._tail.next = newest

        self._tail = newest           # update reference to tail node
        self._size += 1
