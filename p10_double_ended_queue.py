#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


"""
双端队列：
double-ended queue，或deque，发音通常为"deck"；
一个类队列数据结构，支持在队列的头部和尾部都进行插入和删除操作；
双端队列的抽象数据类型比栈和队列的抽象数据类型要更普遍；
Python的标准collections模块中的实现了双端队列类 - deque；

"""


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = 'element', 'previous', 'next'

        def __init__(self, elm, pre, nxt):
            self.element = elm
            self.previous = pre
            self.next = nxt

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header.next = self._trailer
        self._trailer.previous = self._header
        self._size = 0

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)
        predecessor.next = newest
        successor.previous = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete non-sentinel node from the list and return its element."""
        predecessor = node.previous
        successor = node.next
        predecessor.next = successor
        successor.previous = predecessor
        self._size -= 1
        element = node.element
        node.previous = node.next = node.element = None
        return element


class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            return
        return self._header.next.element

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            return
        return self._trailer.previous.element

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header.next)

    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer.previous, self._trailer)

    def delete_first(self):
        """Remove and return the element from the front of the deque."""
        if self.is_empty():
            return
        return self._delete_node(self._header.next)

    def delete_last(self):
        """Remove and return the element from the back of the deque."""
        if self.is_empty():
            return
        return self._delete_node(self._trailer.previous)
