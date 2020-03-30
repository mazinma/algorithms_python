#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen

"""
原理：插入排序的改进版，先按一定间隔分组，每组插入排序，然后缩小间隔继续，直至间隔大小为1；
"""


def shell_sort(array):
    gap = len(array) // 2

    while gap > 0:
        for i in range(gap, len(array)):
            for j in range(i, 0, -gap):
                if array[j] < array[j - gap]:
                    array[j], array[j - gap] = array[j - gap], array[j]

        gap = gap // 2

    return gap


if __name__ == '__main__':
    collection = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(collection)
    print(collection)

"""
插入排序：在排序的过程中，把数组的每一个元素按大小关系，插入到前面的有序区的对应位置；

插入排序的平均时间复杂度是O(n^2);

特点：
（1）在大多数元素已经有序的情况下，插入排序的工作量较小；
（2）在元素较少的情况下，插入排序的工作量较小；


希尔排序：先逐步分组进行粗调，再进行直接插入排序，就是希尔排序，由发明者计算机科学家
Donald Shell的名字所命名；

分组跨度，被称为希尔排序的增量，增量的选择有很多种，逐步折半的增量方法，被称为希尔增量，
希尔增量之间是等比的，这就导致希尔增量存在盲区；

为了保证分组粗调没有盲区，每一轮的增量需要彼此"互质"，也就是没有除1之外的公约数，于是
提出了很多增量方式，其中最具有代表的是Hibbard增量和Sedgewick增量；

Hibbard增量：1，3，7，15……，通项公式：2^k - 1，最坏时间复杂度O(n^(3/2))；

Sedgewick增量：1，5，19，41，……，通项公式：4^k - 3*2^k + 1，最坏时间复杂度O(n^(4/3))；
"""
