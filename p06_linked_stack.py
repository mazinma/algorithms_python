#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


class Stack:
    """栈，一种先进后出的数据结构（单向链表实现）"""

    # 嵌套_Node类
    class _Node:
        """单向链表结点"""
        __slots__ = 'element', 'next'

        def __init__(self, elm, nxt):
            self.element = elm
            self.next = nxt

    def __init__(self):
        """初始化一个空栈"""
        self._head = None
        self._size = 0

    def __len__(self):
        """返回栈中元素的数量"""
        return self._size

    def is_empty(self):
        """栈为空返回True，否则返回False"""
        return self._size == 0

    def push(self, elm):
        """向栈中推入元素"""
        self._head = self._Node(elm, self._head)
        self._size += 1

    def top(self):
        """返回栈顶元素，不弹出"""
        if self.is_empty():
            return
        return self._head.element

    def pop(self):
        """从栈顶弹出元素"""
        if self.is_empty():
            return

        answer = self._head.element
        self._head = self._head.next
        self._size -= 1

        return answer


"""
链式栈性能：
S.push(e) : O(1)
S.pop() : O(1)
S.top() : O(1)
len(S) : O(1)
S.is_empty : O(1)
"""
