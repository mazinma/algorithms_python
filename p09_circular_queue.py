#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


class Queue:
    """Queue implementation using circularly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = 'element', 'next'

        def __init__(self, elm, nxt):
            self.element = elm
            self.next = nxt

    def __init__(self):
        """Create an empty queue."""
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            return

        head = self._tail.next

        return head.element

    def dequeue(self):
        """Remove add return the first element of the queue (i.e., FIFO)."""
        if self.is_empty():
            return

        old_head = self._tail.next

        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = old_head.next

        self._size -= 1

        return old_head.element

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)

        if self.is_empty():
            newest.next = newest
        else:
            newest.next = self._tail.next
            self._tail.next = newest

        self._tail = newest
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail.next
