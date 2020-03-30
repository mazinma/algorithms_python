#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


class _Queue:
    """队列，一种先进后出的数据结构（数组实现）"""

    def __init__(self):
        """初始化一个空队列"""
        self.__data = []

    def is_empty(self):
        """队列为空返回True，否则返回False"""
        return self.__data == []

    def size(self):
        """返回列表中元素的数量"""
        return len(self.__data)

    def enqueue(self, item):
        """向队列中入队一个元素"""
        self.__data.append(item)

    def dequeue(self):
        """从队列中出队一个元素"""
        return None if self.is_empty() else self.__data.pop(0)


if __name__ == '__main__':
    q = _Queue()

    print(q.is_empty())
    print(q.size())

    q.enqueue("Hello World!")
    q.enqueue(3.1415926)
    print(q.is_empty())
    print(q.size())

    print(q.dequeue())
    print(q.is_empty())
    print(q.size())

"""
dequeue中调用了pop(0)，耗时为O(n)，导致低效；
"""


class Queue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

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
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO)."""
        if self.is_empty():
            return

        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
