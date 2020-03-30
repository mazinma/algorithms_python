#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


def recursive_binary_search(array, item):
    if len(array) == 0:
        return False

    middle = len(array) // 2

    if item == array[middle]:
        return True

    if item < array[middle]:
        return recursive_binary_search(array[:middle], item)
    else:
        return recursive_binary_search(array[middle+1:], item)


def non_recursive_binary_search(array, item):
    start, end = 0, len(array) - 1

    while start <= end:
        middle = (start + end) // 2

        if item == array[middle]:
            return True
        elif item < array[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return False


if __name__ == '__main__':
    collection = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(recursive_binary_search(collection, 3))
    print(non_recursive_binary_search(collection, 13))
