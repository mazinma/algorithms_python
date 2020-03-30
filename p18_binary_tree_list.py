#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


def binary_tree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])

    return root


def insert_right(root, new_branch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])

    return root


def get_root_value(root):
    return root[0]


def set_root_value(root, new_value):
    root[0] = new_value


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]