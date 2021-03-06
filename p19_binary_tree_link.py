#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


class BinaryTree:

    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_root_value(self):
        return self.key

    def set_root_value(self, obj):
        self.key = obj


if __name__ == '__main__':
    r = BinaryTree('a')
    r.insert_left('b')
    r.insert_right('c')
    r.get_left_child().insert_right('d')
    r.get_right_child().set_root_value('hello')
