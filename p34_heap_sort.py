#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen

"""
堆排序是利用堆进行排序；

堆是一种完全二叉树，有两种类型：大顶堆、小顶堆；

大顶堆：每个结点的值都大于或等于左右孩子结点；
小顶堆：每个结点的值都小于或等于左右孩子结点；

完全二叉树：除了最后一层之外，每一层都被完全填充，并且所有结点都保持向左对齐的树；

算法思路：
（1）构建完全二叉树，将原始数据放入完全二叉树中；
（2）构建大顶堆，需要选择起点结点，选择下一个结点，以及如何调整；
（3）排序：将堆顶元素依次拿走，生成排序的树，最后用层序遍历就可以拿到所有的排序元素；
"""


def max_heapify(array, i, heap_size=None):
    """
    维护大顶堆性质
    输入包含堆的数组array，以及索引i，使得以下标i为根结点的子树，满足大顶堆性质
    时间复杂度O(h)，h为堆的高度
    """
    if not heap_size:
        heap_size = len(array)  # 默认情况下，array中全是堆元素

    left = 2 * i + 1   # 获取i的左孩子的索引
    right = 2 * i + 2  # 获取i的右孩子的索引

    # 找出孩子树的根结点、左孩子、右孩子中关键字最大的索引
    if left < heap_size and array[left] > array[i]:
        largest = left
    else:
        largest = i

    if right < heap_size and array[right] > array[largest]:
        largest = right

    # 如果最大的关键字的索引不是根结点索引，那么就将最大关键字和根结点交换
    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        max_heapify(array, largest, heap_size)


# 创建一个大顶堆
def build_max_heap(array, heap_size=None):
    """
    输入array中的元素为排列顺序随机的元素（可能不是大顶堆）
    经过该函数处理，保证将array变成大顶堆
    默认情况下，array中全是堆元素
    时间复杂度O(n log n)
    """
    if not heap_size:
        heap_size = len(array)

    i = int(heap_size / 2) - 1  # 获取该堆的最后一个非叶子结点的索引

    # 从最后一个叶子结点依次向前遍历至根结点
    while i >= 0:
        max_heapify(array, i, heap_size)
        i -= 1


# 堆排序
# T(n) = O(n log n)
def heap_sort(array, heap_size=None):
    # 默认情况下，array中全是堆元素
    if not heap_size:
        heap_size = len(array)

    # 将a维护成一个大顶堆
    build_max_heap(array)
    start = heap_size - 1

    # 从array第一个元素开始遍历
    for i in range(start, 0, -1):
        array[0], array[i] = array[i], array[0]  # 将遍历到的元素与最后一个堆元素交换
        heap_size -= 1
        max_heapify(array, 0, heap_size=heap_size)  # 堆元素减1后，维护大顶堆性质


if __name__ == '__main__':
    collection = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    heap_sort(collection)
    print(collection)
