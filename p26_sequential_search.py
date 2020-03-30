#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


def sequential_search(array, item):
    position = 0
    found = False

    while position < len(array) and not found:
        if array[position] == item:
            found = True
        else:
            position += 1

    return found


if __name__ == '__main__':
    collection = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequential_search(collection, 3))
    print(sequential_search(collection, 13))
