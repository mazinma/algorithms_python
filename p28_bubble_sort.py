#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen

"""
原理：
（1）比较相邻的元素。如果第一个比第二个大，就交换它们两个；
（2）对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数；
（3）针对所有的元素重复以上步骤，除了最后一个；
（4）持续每次对越来越少的元素重复以上步骤，直到没有任何一对数字需要比较；
"""


def bubble_sort(array):
    for i in range(len(array) - 1):
        count = 0

        for j in range(len(array)-1, 0, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                count += 1

        if count == 0:
            break


if __name__ == '__main__':
    collection = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(collection)
    print(collection)
