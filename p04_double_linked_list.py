#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


class Node:
    """双向链表结点"""

    def __init__(self, item):
        """初始化一个新结点"""
        self.item = item
        self.previous = None
        self.next = None


class DoubleLinkedList:
    """双向链表"""

    def __init__(self):
        """初始化链表，定义头结点"""
        self.__head = None

    def is_empty(self):
        """链表为空返回True，否则返回False"""
        return self.__head is None

    def length(self):
        """链表的长度（结点数）"""
        cursor = self.__head
        count = 0

        while cursor is not None:
            count += 1
            cursor = cursor.next

        return count

    def travel(self):
        """遍历链表"""
        cursor = self.__head

        while cursor is not None:
            print(cursor.item, end=" ")
            cursor = cursor.next

        print()

    def add(self, item):
        """链表头部添加结点"""
        node = Node(item)

        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.previous = node
            self.__head = node

    def append(self, item):
        """链表尾部添加结点"""
        node = Node(item)

        if self.is_empty():
            self.__head = node
        else:
            cursor = self.__head

            while cursor.next is not None:
                cursor = cursor.next

            node.previous = cursor
            cursor.next = node

    def insert(self, position, item):
        """链表指定位置插入结点"""
        if position <= 0:
            self.add(item)
        elif position > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cursor = self.__head
            index = 0

            while index < position - 1:
                index += 1
                cursor = cursor.next

            node.next = cursor.next
            node.previous = cursor
            cursor.next.previous = node
            cursor.next = node

    def remove(self, item):
        """删除结点"""
        cursor = self.__head

        while cursor is not None:
            if cursor.item == item:
                # 处理previous指针
                if cursor.previous is None:
                    self.__head = cursor.next
                else:
                    cursor.previous.next = cursor.next

                # 处理next指针
                if cursor.next is not None:
                    cursor.next.previous = cursor.previous

                return

            cursor = cursor.next

    def search(self, item):
        """查找结点"""
        cursor = self.__head

        while cursor is not None:
            if cursor.item == item:
                return True

            cursor = cursor.next

        return False


if __name__ == '__main__':
    d = DoubleLinkedList()

    print(d.is_empty(), d.length())

    d.add("Stephen Curry")
    d.add("Ray Allen")
    print(d.length())
    d.travel()

    d.append("Kobe Bryant")
    print(d.length())
    d.travel()

    d.insert(2, "Black Mamba")
    print(d.length())
    d.travel()

    print(d.search("Ray Allen"))
    d.remove("Black Mamba")
    print(d.length())
    d.travel()
