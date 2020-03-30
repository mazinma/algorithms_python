#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


"""
堆：
（1）堆是一颗完全二叉树，完全二叉树就是只有最后一层有叶子结点，而且叶子结点是靠左排列的；
（2）堆中的每一个结点都大于其左右子结点（大顶堆），或每个结点都小于其左右子结点（小顶堆）；

插入元素：
（1）插入过程确保两点：一、确保它是完全二叉树，二、确保符合大顶堆（小顶堆）；
（2）完全二叉树使用数组存储，只要在数组的最后插入新元素，让其与父结点比较，如果大于父结点，
则与父结点交换，直到小于父结点或到达要找到的结点为止；

删除元素：
（1）删除堆顶元素后，将数组的最后一个元素放到堆顶位置，然后从上到下进行堆化，这样就可以保证
在删除的过程中仍然是一个完全二叉树；
（2）堆化就是将当前结点与左右子结点进行比较，如果小于子结点，则与其交换，直到满足大顶堆位置
条件；
"""


class Heap:

    def __init__(self):
        """初始化一个空堆"""
        self.data = []

    def get_parent_index(self, index):
        """返回父结点的下标"""
        if index == 0 or index > (len(self.data) - 1):
            return None
        return index - 1 >> 1

    def swap(self, index_a, index_b):
        """交换堆中的两个元素"""
        self.data[index_a], self.data[index_b] = self.data[index_b], self.data[index_a]

    def insert(self, item):
        """
        先将元素放在最后，然后从后往前依次堆化；
        以大顶堆为例，如果插入元素比父结点大，则交换，直到不能交换为止；
        """
        self.data.append(item)
        index = len(self.data) - 1
        parent = self.get_parent_index(index)

        # 循环，直到该元素成为堆顶，或小于父结点（对于大顶堆）
        while parent is not None and self.data[parent] < self.data[index]:
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(parent)

    def remove_max(self):
        """删除堆顶元素，然后将最后一个元素放在堆顶，再自上向下依次堆化"""
        remove = self.data[0]
        self.data[0] = self.data[-1]
        del self.data[-1]

        self.heapify(0)
        return remove

    def heapify(self, index):
        """自上向下堆化，从index开始堆化操作（大顶堆）"""
        total = len(self.data) - 1

        while True:
            max_value_index = index

            if 2 * index + 1 <= total and self.data[2 * index + 1] > self.data[max_value_index]:
                max_value_index = 2 * index + 1

            if 2 * index + 2 <= total and self.data[2 * index + 2] > self.data[max_value_index]:
                max_value_index = 2 * index + 2

            if max_value_index == index:
                break

            self.swap(index, max_value_index)
            index = max_value_index


if __name__ == '__main__':
    h = Heap()

    for i in range(10):
        h.insert(i + 1)

    print("建堆：", h.data)
    print("删除堆顶元素：", [h.remove_max() for i in range(10)])


"""
删除堆顶数据：O(log n);
向堆中插入数据：O(log n)；


堆的应用：
（1）堆排序：分建堆和排序两个过程；
    建堆：插入元素的过程，可以对初始数组原地建堆，时间复杂度O(n)；
    排序：依次输出堆顶元素即可达到排序的目的，时间复杂度O(n log n)；

    堆排序是不稳定的排序算法，因为在排序过程中，存在将堆的最后一个元素跟堆顶元素交换的操作，可能改变原始相对顺序；

（2）优先级队列：
    队列：一种先进先出（FIFO）的数据结构；
    优先级队列：一种特殊的队列，队列出队顺序非先进先出，而是优先级高的先出；

    优先级队列的实现：有很多中方法，用堆实现是最直接、最高效的，因为堆和优先级队列非常相似，一个堆即一个优先级队列
    很多时候只是概念上的区分。向优先级队列中插入一个元素，相当于向堆中插入一个元素；从优先级队列中取出一个元素，相当
    于弹出堆顶元素；

    a、合并有序小文件。
    假如有100个小文件，每个都是100MB，每个中存储的都是有序的字符串，现要合并成一个有序的大文件，该如何做？
    
    直观的做法是，分别取每个小文件的第一行放入数组，再比较大小，依次插入到大文件中，假如最小的行来自于文件a，那么插入
    到大文件中后，从数组中删除改行，再取文件a的下一行插入到数组中，再次比较大小，取出最小的插入到大文件的第二行，以此
    类推，整个过程很像归并排序的合并函数。每次插入到大文件中都要循环遍历整个数组，这显然是低效的；
    
    而借助于堆这种优先级队列就很高效。比如，分别取100个文件的第一行建一个小顶堆，假如堆顶元素来自于文件a，那么取出堆顶
    的元素插入到大文件中，并从堆顶删除该元素（就是堆实现removeMax函数），然后再从文件a中取下一行插入到堆顶中，重复以上
    过程就可以完成合并有序小文件的操作；

    b、高性能定时器。
    假如有很多定时任务，如何设计一个高性能的定时器来执行这些定时任务呢？

    假如每过一个很小的单位时间（比如1秒），就扫描一遍任务，看是否有任务到达设定的执行时间。如果到达了，就拿出来执行。这
    显然是浪费资源的，因为这些任务的时间间隔可能长达数小时；

    借助于堆这种优先级队列，可以这样设计：将定时任务按时间先后顺序建立一个小顶堆，先取出堆顶任务，查询其执行时间与当前时间
    之差，假如为T秒，那么在T-1秒的时间内，定时器什么也不需要做，当T秒时间间隔达到时，就取出任务执行，对应的从堆顶删除堆顶
    元素，然后取出下一个堆顶元素，查询其执行时间。这样，定时器既不用间隔1秒就轮询一次，也不用遍历整个任务列表，提高了性能。

（3）取top k 元素；
（4）取中位数；
"""
