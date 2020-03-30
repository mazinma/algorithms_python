#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen

"""
原理：
（1）申请空间，使其大小为两个已经排序序列只和，该空间用来存放合并后的序列；
（2）设定两个指针，最初位置分别为两个已经排序序列的起始位置；
（3）比较两个指针所指向的元素，选择相对较小的元素放入到合并空间，并移动指针到下一个位置；
（4）重复步骤（3）直到某一指针超出序列；
（5）将另一序列剩下的所有元素直接复制到合并序列尾；
"""


def merge_sort(array):
    # 递归退出条件
    if len(array) <= 1:
        return array  # 注意：有返回值

    mid = len(array) // 2
    left_list = merge_sort(array[0:mid])
    right_list = merge_sort(array[mid:len(array)])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    """将左右两个有序数列依次取比较大的那个元素，放入新序列"""
    left, right = 0, 0  # 定义左右两个序列的起始元素位置
    result = list()

    # 循环退出条件：一侧遍历完，另一侧剩余元素直接添加至队尾
    while left < len(left_list) and right < len(right_list):
        if left_list[left] < right_list[right]:
            result.append(left_list[left])
            left += 1
        else:
            result.append(right_list[right])
            right += 1

    result += left_list[left:]
    result += right_list[right:]

    return result


if __name__ == '__main__':
    collection = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(merge_sort(collection))
