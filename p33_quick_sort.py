#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


"""
原理：找一个基准元素，将所有小于基准元素的放置一侧，大于（等于）基准元素的放置另一侧，
递归，直至列表大小为0或1，即肯定有序；


分治策略：
指的是将原问题分解为若干规模更小，但结构和原理与原问题相似的子问题。递归地解决这些子
问题，然后将这些子问题的解组合为原问题的解；
"""


def _quick_sort(array):
    if len(array) < 2:
        return array

    else:
        pivot = array.pop()
        less_than_pivot = [x for x in array if x < pivot]
        more_than_pivot = [x for x in array if x >= pivot]
        return _quick_sort(less_than_pivot) + [pivot] + _quick_sort(more_than_pivot)


"""
上面这段代码里，最关键的是pivot这个参数，虽然代码短小利于理解，但是效率极低，主要体现在：
（1）分组基准的选择过于随便，不一定可以取到列表的中间值；
（2）空间复杂度大，使用了两个列表解析，而且每次选值比较时，需要遍历整个序列；
（3）若序列长度过于小（比如只有几个元素），快速排序的效率就不如插入排序；
（4）递归影响性能；
"""


def quick_sort(array):
    return sort(array, 0, len(array)-1)


def sort(array, left, right):
    if left < right:
        pivot = partition(array, left, right)
        sort(array, left, pivot-1)
        sort(array, pivot+1, right)

    return array


def partition(array, left, right):
    pivot_key = array[left]

    while left < right:
        while left < right and array[right] >= pivot_key:
            right -= 1

        array[left] = array[right]

        while left < right and array[left] <= pivot_key:
            left += 1

        array[right] = array[left]

    array[left] = pivot_key
    return left


if __name__ == '__main__':
    collection = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(collection)
    print(collection)
