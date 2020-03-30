#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen

"""
原理：将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据；
"""


def insertion_sort(array):
    for index in range(1, len(array)):
        current = array[index]
        position = index

        while position > 0 and array[position-1] > current:
            array[position] = array[position-1]
            position = position - 1

        array[position] = current


if __name__ == '__main__':
    collection = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(collection)
    print(collection)
