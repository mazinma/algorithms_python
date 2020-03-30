#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


class HashTable:
    """
    self.slots: 列表，储存键；
    self.data: 列表，储存值；
    当通过键查找值时，键在self.slots中的index，即为值在self.data中的index；
    """

    def __init__(self):
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        # 如果slots当前的hash_value位置上的值为None，则插入新值
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            # 如果slots当前的hash_value位置上的值为key，则用新值代替旧值
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                # 如果slots当前的hash_value位置上的值为其它的值，则开始探测后面的位置
                next_slot = self.rehash(hash_value, len(self.slots))

                # 如果一个位置不为空且不等于当前值，即被其它值占用，则继续探测后面一个
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                # 如果后一个值为空，则插入，为原来的值，则替换；
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.slots[next_slot] = data
                else:
                    self.data[next_slot] = data

    @staticmethod
    def hash_function(key, size):
        """余数法计算hash_value"""
        return key % size

    @staticmethod
    def rehash(old_hash, size):
        """使用+1法rehash"""
        return (old_hash+1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data, stop, found, position = None, False, False, start_slot

        while self.slots[position] is not None and (not found) and (not stop):
            # 如果slots当前位置上的值等于key，则找到了对应的value
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                # rehash后继续搜寻下一个可能的位置
                position = self.rehash(position, len(self.slots))

            # 如果最后又回到了第一次搜寻的位置，则要找的key不再slots中
            if position == start_slot:
                stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
