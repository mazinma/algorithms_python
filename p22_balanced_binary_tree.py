#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


"""
平衡二叉树：Balanced Binary Tree，又称AVL树；
是一种特殊的二叉排序树，它或者是空树，或者每个结点的左右子树都是平衡二叉树，也就是每个
结点的左右子树的高度之差只能是-1，0，1三种情况；


平衡状况由平衡因子（Balance Factor，BF）来衡量。平衡因子定义为当前结点的左右子树的高
度之差，如果能够维持平衡二叉树，检索操作就能在O(log n)时间内完成；


需要调整的情况分四种：
（1）LL型调整：树a的左子树较高，新结点插入在a的左子树的左子树。进行右旋转；
（2）RR型调整：树a的右子树较高，新结点插入在a的右子树的右子树。进行左旋转；
（3）LR型调整：树a的左子树较高，新结点插入在a的左子树的右子树。先进行左旋转，再右旋转；
（4）RL型调整：树a的右子树较高，新结点插入在a的右子树的左子树。先进性右旋转，再左旋转；
"""


class StackUnderflow(ValueError):
    pass


class Stack:

    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements is None

    def top(self):
        if self.elements is None:
            raise StackUnderflow("in Stack.top()")
        return self.elements[-1]

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.elements is None:
            raise StackUnderflow("in Stack.pop()")
        return self.elements.pop()


class Association:
    """一个关联类"""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):  # Python解释器遇到比较运输算符"<"，会去找类里定义的__lt__方法
        return self.key < other.key

    def __le__(self, other):  # less than or equal to
        return self.key < other.key or self.key == other.key

    def __str__(self):
        return "Association({0},{1})".format(self.key, self.value)


class BinaryTreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class DictBinaryTree:

    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root is None

    def search(self, key):
        """检索是否存在关键码key"""
        bt = self.root

        while bt is not None:
            entry = bt.data

            if key < entry.key:
                bt = bt.left
            elif key > bt.right:
                bt = bt.right
            else:
                return entry.value

        return None

    def insert(self, key, value):
        bt = self.root

        if bt is None:
            self.root = BinaryTreeNode(Association(key, value))
            return

        while True:
            entry = bt.data

            # 如果小于当前关键码，转向左子树
            if key < entry.key:
                # 如果左子树为空，直接将数据插在这里
                if bt.left is None:
                    bt.left = BinaryTreeNode(Association(key, value))
                    return

                bt = bt.left
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BinaryTreeNode(Association(key, value))
                    return

                bt = bt.right
            else:
                bt.data.value = value
                return

    def print_all_values(self):
        bt, s = self.root, Stack()

        while bt is not None or not s.is_empty():
            while bt is not None:
                s.push(bt)
                bt = bt.left

            bt = s.pop()  # 将栈顶元素弹出
            yield bt.data.key, bt.data.vlaue
            bt = bt.right  # 将当前结点的右子结点赋值给bt，让其在while中继续压入栈

    def entries(self):
        bt, s = self.root, Stack()

        while bt is not None or not s.is_empty():
            while bt is not None:
                s.push(bt)
                bt = bt.left

            bt = s.pop()
            yield bt.data.key, bt.data.value
            bt = bt.right

    def print_key_value(self):
        for k, v in self.entries():
            print(k, v)

    def delete(self, key):
        del_position_father, del_position = None, self.root  # 待删结点和其父结点

        while del_position is not None and del_position.data.key != key:
            del_position_father = del_position

            if key < del_position.data.key:
                del_position = del_position.left
            else:
                del_position = del_position.right

            if del_position is None:
                print("There is no key")
                return

        # 如果待删结点只有右子树
        if del_position.left is None:
            if del_position_father is None:
                self.root = del_position.right
            elif del_position is del_position_father.left:
                del_position_father.left = del_position.right
            else:
                del_position_father.right = del_position.right
            return

        pre_node_father, pre_node = del_position, del_position.left

        while pre_node.right is not None:
            pre_node_father = pre_node
            pre_node = pre_node.right

        del_position.data = pre_node.data

        if pre_node_father.left is pre_node:
            pre_node_father.left = pre_node.left

        if pre_node_father.right is pre_node:
            pre_node_father.right = pre_node.left


def build_dict_binary_tree(entries):
    d = DictBinaryTree()

    for k, v in entries:
        d.insert(k, v)

    return d


class AVLNode(BinaryTreeNode):

    def __init__(self, data):
        BinaryTreeNode.__init__(self, data)
        self.bf = 0


class DictAVL(DictBinaryTree):

    def __init__(self, data):
        DictBinaryTree.__init__(self, data)

    @staticmethod
    def ll(a, b):
        a.left = b.right  # 将b的右子树接到a的左子树结点上
        b.right = a       # 将a树接到b的右子结点上
        a.bf = b.bf = 0   # 调整a，b的bf值
        return b

    @staticmethod
    def rr(a, b):
        a.right = b.left
        b.left = a
        a.bf = b.bf = 0
        return b

    @staticmethod
    def lr(a, b):
        c = b.right
        a.left, b.right = c.right, c.left
        c.left, c.right = b, a

        # c本身就是插入点
        if c.bf == 0:
            a.bf = b.bf = 0
        # 插在c的左子树
        elif c.bf == 1:
            a.bf = -1
            b.bf = 0
        # 插在c的右子树
        else:
            a.bf = 0
            b.bf = 1

        c.bf = 0
        return c

    @staticmethod
    def rl(a, b):
        c = b.left
        a.right, b.left = c.left, c.right
        c.left, c.right = a, b

        if c.bf == 0:
            a.bf = b.bf = 0
        elif c.bf == 1:
            a.bf = 0
            b.bf = -1
        else:
            a.bf = 0
            b.bf = 0

        c.bf = 0
        return c

    def insert(self, key, value):
        a = p = self.root

        # 如果根结点为空，则直接插入到根结点
        if a is None:
            self.root = AVLNode(Association(key, value))

        a_father, p_father = None, None  # a_father用于最后将调整后的子树接到其子结点上

        # 通过不断循环，将p下移，查找插入位置，和最小非平衡子树
        while p is not None:
            # 如果key已存在，直接修改其关联值
            if key == p.data.key:
                p.data.value = value
                return

            # 如果当前p结点的BF=0，则有可能是最小非平衡子树的根结点
            if p.bf != 0:
                a_father, a = p_father, p

            p_father = p

            if key < p.data.key:
                p = p.left
            else:
                p = p.right

        # 结束循环后，p_father已经是插入的父结点，a_father和a记录着最小非平衡子树
        node = AVLNode(Association(key, value))

        if key < p_father.data.key:
            p_father.left = node
        else:
            p_father.right = node

        # 新结点已插入，a是最小非平衡子树的根结点
        # 新结点在a的左子树
        if key < a.data.key:
            p = b = a.left
            d = 1  # d记录新结点被插入到a的那颗子树
        # 新结点在a的右子树
        else:
            p = b = a.right
            d = -1

        # 在新结点插入后，修改b到新结点路径上各结点的BF值，调整过程的BF值修改都在子函数中操作
        while p != node:
            if key < p.data.key:
                p.bf = 1
                p = p.left
            else:
                p.bf = -1
                p = p.right

        # 如果a的BF原来为0，那么插入新结点后不会失衡
        if a.bf == 0:
            a.bf = d
            return

        # 如果新结点插入在a较低的子树里
        if a.bf == -d:
            a.bf = 0
            return

        # 以上两个条件均不符，说明新结点被插入在较高的子树里，需要进行调整
        # 如果新结点插入在a的左子树
        if d == 1:
            # b的BF原来为0，如果等于1，说明新结点插入在b的左子树
            if b.bf == 1:
                b = DictAVL.ll(a, b)
            # 新结点插入在b的右子树
            else:
                b = DictAVL.lr(a, b)
        # 新结点插入在a的右子树
        else:
            # 新结点插入在b的右子树
            if b.bf == -1:
                b = DictAVL.rr(a, b)
            # 新结点插入在b的左子树
            else:
                b = DictAVL.rl(a, b)

        # 将调整后的最小非平衡子树接到原树上，即接到原来a结点的父结点上
        # 判断a是否是根结点
        if a_father is None:
            self.root = b
        else:
            if a_father == a:
                a_father.left = b
            else:
                a_father.right = b


if __name__ == '__main__':
    # LL调整
    entire = [(5, "a"), (2.5, "g"), (2.3, "h"), (3, "b"), (2, "d"), (4, "e"), (3.5, "f")]
    dictionary = build_dict_binary_tree(entire)
    dictionary.print_key_value()
    print("after inserting")
    dictionary.insert(1, "i")
    dictionary.print_key_value()

    # LR调整
    entire = [(2.5, "g"), (3, "b"), (4, "e"), (3.5, "f")]
    dictionary = build_dict_binary_tree(entire)
    dictionary.print_key_value()
    print("after inserting")
    dictionary.insert(3.2, "i")
    dictionary.print_key_value()
