#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


class Stack:
    """栈，一种先进后出的数据结构（数组实现）"""

    def __init__(self):
        """初始化一个空栈"""
        self.__data = list()  # 用Python中的list实现

    def is_empty(self):
        """栈为空返回True，否则返回False"""
        return self.__data == []

    def size(self):
        """返回栈中元素的数量"""
        return len(self.__data)

    def push(self, item):
        """向栈顶添加元素"""
        self.__data.append(item)

    def pop(self):
        """从栈顶弹出元素"""
        return None if self.is_empty() else self.__data.pop()

    def top(self):
        """返回栈顶元素，不弹出"""
        return None if self.is_empty() else self.__data[-1]


if __name__ == '__main__':
    s = Stack()

    print(s.is_empty())
    print(s.size())

    s.push("Hello World!")
    s.push("This is Allen")
    print(s.is_empty())
    print(s.size())
    print(s.top())

    print(s.pop())
    print(s.is_empty())
    print(s.size(), s.top())

"""
性能：
S.push(e) : O(1)
S.pop() : O(1)
S.top() : O(1)
S.is_empty() : O(1)
S.size() : O(1)


Python的列表和元组类：列表的non-mutating行为是由元组（tuple）类所支持的；

列表和元组类中non-mutating行为的渐进性能：
len(data) : O(1)
data[j] : O(1)
data.count(value) : O(n)
data.index(value) : O(k + 1)  # k表示被搜索值在最左边出现时的索引
value in data : O(k + 1)
data1 = data2 : O(k+1)  (similarly !=, <, <=, >, >=)
data[j:k] : O(k-j+1)
data1 + data2 : O(n1 + n2)
C*data : O(cn)

列表类变异行为的渐进性能：
data[j] = val : O(1)
data.append(value) : O(1)*
data.insert(k, value) : O(n-k+1)*
data.pop() : O(1)*
data.pop(k)、del data[k] : O(n-k)*
data.remove(value) : O(n)*
data1.extend(data2)、data1 += data2 : O(n2)*
data.reverse() : O(n)
data.sort() : O(n log n)
"""
