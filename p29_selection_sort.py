#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen

"""
原理：
（1）第一次从待排序的元素中选出最小（或最大）的一个元素，存放在序列的起始位置；
（2）然后再从剩余的未排序元素中寻找到最小（大）的元素，然后放到已排序的序列末尾；
（3）依次类推，直到全部待排序的数据元素的个数为零；
"""


def selection_sort(array):
    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    collection = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(collection)
    print(collection)
