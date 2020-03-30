#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


class Node:
    """单向循环链表结点"""

    def __init__(self, item):
        """初始化一个新结点"""
        self.item = item
        self.next = None


class SingleCycleLinkedList:
    """单向循环链表"""

    def __init__(self):
        """初始化一个链表， 定义头结点"""
        self.__head = None

    def is_empty(self):
        """链表为空返回True，否则返回False"""
        return self.__head is None

    def length(self):
        """链表的长度（结点数）"""
        if self.is_empty():
            return 0

        cursor = self.__head
        count = 1

        while cursor.next != self.__head:
            count += 1
            cursor = cursor.next

        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return

        cursor = self.__head

        while cursor.next != self.__head:
            print(cursor.item, end=" ")
            cursor = cursor.next

        print(cursor.item)

    def add(self, item):
        """链表头部添加结点"""
        node = Node(item)
        cursor = self.__head

        if self.is_empty():
            self.__head = node
            node.next = node
            return

        while cursor.next != self.__head:
            cursor = cursor.next

        node.next = self.__head
        cursor.next = node

    def append(self, item):
        """链表尾部添加结点"""
        if self.is_empty():
            self.add(item)
            return

        node = Node(item)
        cursor = self.__head

        while cursor.next != self.__head:
            cursor = cursor.next

        node.next = self.__head
        cursor.next = node

    def insert(self, position, item):
        """链表指定位置添加结点"""
        if position <= 0:
            self.add(item)
        elif position > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cursor = self.__head
            index = 0

            while index < position - 1:
                cursor = cursor.next
                index += 1

            node.next = cursor.next
            cursor.next = node

    def remove(self, item):
        """
        删除结点

        1、删除头结点：（1）链表只有一个结点；（2）链表有多个结点；
        2、删除非头结点：（1）一般结点；（2）尾结点；

        """
        if self.is_empty():
            return

        cursor = self.__head
        previous = None

        # 要删除的结点是头结点
        if cursor.item == item:
            while cursor.next != self.__head:
                previous = cursor
                cursor = cursor.next

            # 链表只有一个结点
            if previous is None:
                self.__head = None
            # 链表有多个结点
            else:
                cursor.next = self.__head.next
                self.__head = self.__head.next
        # 要删除的结点非头结点
        else:
            # 遍历链表
            while cursor.next != self.__head:
                # 找到要删除的结点
                if cursor.item == item:
                    previous.next = cursor.next
                    return
                # 未找到要删除的结点
                else:
                    previous = cursor
                    cursor = cursor.next

            # 要删除的结点为尾结点
            if cursor.item == item:
                previous.next = self.__head

    def search(self, item):
        """查找结点"""
        if self.is_empty():
            return False

        cursor = self.__head

        while cursor.next != self.__head:
            if cursor.item == item:
                return True

            cursor = cursor.next

        return True if cursor.item == item else False


if __name__ == '__main__':
    s = SingleCycleLinkedList()

    print(s.is_empty(), s.length())

    s.add("Stephen Curry")
    s.add("Ray Allen")
    print(s.length())
    s.travel()

    s.append("Kobe Bryant")
    print(s.length())
    s.travel()

    s.insert(1, "Tony Parker")
    print(s.length())
    s.travel()

    print(s.search("Ray Allen"))
    s.remove("Tony Parker")
    print(s.length())
    s.travel()
