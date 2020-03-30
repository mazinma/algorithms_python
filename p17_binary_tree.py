#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


"""
二叉树：树有一个根结点，每个结点最多有两个子结点；

二叉树深度优先遍历根据遍历顺序不同可以分为三类：
先序遍历：先访问根结点，再访问左结点，最后访问右结点；
中序遍历：先访问左结点，再访问根结点，最后访问右结点；
后序遍历：先访问左结点，再访问右结点，最后访问根结点；
注意：左结点永远在右结点前面，先、中、后可以理解为先、中、后地访问根节点；

一般情况下：深度优先用递归，广度优先用队列；
"""


class Node:
    """二叉树结点"""

    def __init__(self, item):
        self.item = item
        self.left_child = None
        self.right_child = None


class Tree:
    """(满)二叉树"""

    def __init__(self):
        """初始化二叉树，定义根节点"""
        self.__root = None

    @property
    def root(self):
        return self.__root

    def add(self, item):
        """添加结点"""
        node = Node(item)

        if self.__root is None:
            self.__root = node
        else:
            queue = list()
            queue.append(self.__root)  # 将头结点加入队列

            while queue:
                cursor = queue.pop()

                if cursor.left_child is None:  # 左孩子结点为空，在此处添加新结点
                    cursor.left_child = node
                    return

                if cursor.right_child is None:  # 左孩子结点不为空时，右孩子结点为空，在此处添加新结点
                    cursor.right_child = node
                    return

                # 左右结点都不为空， 将左右结点添加到队列尾，递归判断，直到将新结点添加至树中
                queue.append(cursor.left_child)
                queue.append(cursor.right_child)

    def pre_order(self, root):
        """递归实现先序遍历"""
        if root is None:
            return

        print(root.item)
        self.pre_order(root.left_child)
        self.pre_order(root.right_child)

    def in_order(self, root):
        """递归实现中序遍历"""
        if root is None:
            return

        self.in_order(root.left_child)
        print(root.item)
        self.in_order(root.right_child)

    def post_order(self, root):
        """递归实现后序遍历"""
        if root is None:
            return

        self.post_order(root.left_child)
        self.post_order(root.right_child)
        print(root.item)

    def breadth_travel(self):
        """广度优先遍历"""
        if self.__root is None:
            return

        queue = list()
        queue.append(self.__root)

        while queue:
            node = queue.pop(0)
            print(node.item)
            if node.left_child is not None:
                queue.append(node.left_child)
            if node.right_child is not None:
                queue.append(node.right_child)


if __name__ == '__main__':
    t = Tree()

    t.add("Stephen Curry")
    t.add("Kobe Bryant")
    t.add("Tony Parker")
    t.add("Ray Allen")
    t.add("Yao")
    t.add("Sun")
    t.add("Yi")

    t.pre_order(t.root)
    t.in_order(t.root)
    t.post_order(t.root)
    t.breadth_travel()
