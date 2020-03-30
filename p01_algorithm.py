#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen

"""
题目：求满足条件的所有a、b、c组合：a+b+c=1000，a^2+b^2=c^2。
"""

import time


def func1():
    start = time.time()

    for i in range(1000):
        for j in range(1000):
            for k in range(1000):
                if i + j + k == 1000 and i * i + j * j == k * k:
                    print(f'i={i}, j={j}, k={k}')

    end = time.time()

    print(f'Time func1 spend：{end-start}')


def func2():
    start = time.time()

    for i in range(1000):
        for j in range(1000):
            k = 1000 - i - j
            if i * i + j * j == k * k:
                print(f'i={i}, j={j}, k={k}')

    end = time.time()

    print(f'Time func2 spend：{end-start}')


if __name__ == '__main__':
    func1()
    func2()


"""
分析：根据时间复杂度计算规则，func1()的时间复杂度为O(n^3)，而func2的为O(n^2)，
因为此处n=1000，所以两者相差近3个数量级。
"""
