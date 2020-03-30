#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


"""
二叉搜索树：Binary Search Tree，BST，又称"二叉排序树"；
左子树上所有结点的值均小于根结点的值，右子树所有结点的值均大于根节点的值，左小右大，并非乱序；

二叉搜索树的产生原因，它的用途？
有了二叉搜素树，当需要查找一个值时，无需遍历整个序列或整棵树，根据当前遍历到的结点的值来确定
搜索方向，每次都会把搜索范围缩小，类似二分查找的思想；

二叉搜索树可以使查找、插入的效率大大提高，为什么还要引入二叉平衡树？
（1）二叉搜索树的结构与值的插入顺序有关，同一数组，若元素的插入顺序不同，二叉搜索树的结构是
千差万别的；
（2）插入的顺序越接近有序，生成的二叉搜索树就越像一个链表；
（3）为了避免二叉搜索树变成"链表"，引入平衡二叉树，让树的结构尽量"均匀"，左右子树的结点树尽量
一样多；

平衡二叉树：Balanced Binary Tree，AVL树；
左子树上所有结点的值均小于根结点的值，右子树上所有结点的值均大于根结点的值，且左右子树高度差最
大为1；

生成平衡二叉树
先按照生成二叉搜索树的方法构造二叉树，直至二叉树变得不平衡，即出现这样的结点：左右子树的高度差
大于1，至于如何调整，要看插入的导致二叉树不平衡的结点的位置。主要有四种调整方式：LL（左旋）、
RR（右旋）、LR（先左旋再右旋）、RL（先右旋再左旋）；

复杂度：
算法、平均、最差
（1）空间、O(n)、O(n)；
（2）查找、O(log n)、O(n)；
（3）插入、O(log n)、O(n);
（4）删除、O(log n)、O(n);

查找步骤：
向一个二叉搜索树插入结点s的算法，过程为：
（1）若B是空树，则将s所指结点作为根结点插入；
（2）若 s ——> data 等于B的根结点的数据域的值，则返回；
（3）若 s ——> data 小于B的根结点的数据域的值，则把s所指的结点插入到左子树中；
（4）把s所指结点插入到右子树中（新插入的结点总是叶子结点）；

删除步骤：
从BST中删除结点比插入结点难度大，因为删除一个非叶子结点，就必须选择其它结点来填补因删除结点所
造成的树的断裂。如果不选择结点来填补这个断裂，就违背了BST的性质要求；

删除结点算法的第一步是要定位被删除的结点，可以使用查找算法，运行时间为O(log 2 n)，然后选择合适
的结点来替代删除结点的位置，共有3中情况需要考虑：
（1）若被删除结点为叶子结点，即该结点的左右子树均为空，由于删除叶子结点不会破坏整颗树的结构，则
只需修改其双亲结点的指针即可；
（2）若被删除的结点只有左子树或右子树，此时只要让左子树或右子树直接成为其双亲结点的左子树或右子树
即可，该修改也不会破坏二叉查找树的特性；
（3）若被删除的结点左右子树均不为空，如果被删除结点的右孩子没有左孩子，那么这个右孩子被用来替换被
删除结点，因为被删除结点的右孩子都大于被删除结点左子树的所有结点，同时也大于或小于被删除结点的父结
点，着取决于被删除结点是左孩子还是右孩子。因此，用右孩子来替换被删除结点，符合二叉查找树的性质。如
果被删除结点的右孩子有左孩子，就需要用被删除结点右孩子的左子树的最下面的结点来替换它，总之，用被删
结点的右子树中的最小值的结点来替换；
"""


class Node:
    """二叉查找树结点"""

    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTree:
    """二叉查找树"""

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def find(self, key):
        if self.root:
            result = self._find(key, self.root)

            if result:
                return result
            return None

    def _find(self, key, node):
        if not node:
            return None
        elif node.data == key:
            return node
        elif key < node.data:
            return self._find(key, node.left)
        else:
            return self._find(key, node.right)

    def insert(self, key):
        node = Node(key)

        if not self.root:
            self.root = node
            self.size += 1
        else:
            current_node = self.root

            while True:
                if key < current_node.data:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = node
                        node.parent = current_node
                        self.size += 1
                        break
                elif key > current_node.data:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = node
                        node.parent = current_node
                        self.size += 1
                        break
                else:
                    break

    def find_min(self):
        if self.root:
            return self._find_min(self.root)

    @staticmethod
    def _find_min(node):
        if node:
            current_node = node

            while current_node.left:
                current_node = current_node.left

            return current_node

    def find_max(self):
        if self.root:
            current_node = self.root

            while current_node:
                current_node = current_node.right

            return current_node
        else:
            return None

    def delete(self, key):
        if self.size > 1:
            node_to_delete = self.find(key)

            if node_to_delete:
                self._delete(node_to_delete)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.data == key:
            self.root = Node(None)
            self.size = 0
        else:
            raise KeyError("Error, key not in tree")

    def _delete(self, node):
        # node为树叶结点
        if not node.left and node.right:
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        # node有两个儿子
        elif node.right and node.left:
            min_node = self._find_min(node.right)
            node.data = min_node.data
            self._delete(min_node)
        # node有一个儿子
        else:
            if node.left:
                # node为父结点的左子树
                if node.parent and node.parent.left == node:
                    node.left.parent = node.parent
                    node.parent.left = node.left
                # node为父结点的右子树
                elif node.parent and node.parent.right == node:
                    node.left.parent = node.parent
                    node.parent.right = node.left
                # node为根结点
                else:
                    self.root = node.left
                    node.left.parent = None
            else:
                if node.parent and node.parent.left == node:
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.parent and node.parent.right == node:
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:
                    self.root = node.right
                    node.right.parent = None
                    node.right = None

    def print_tree(self):
        if self.size == 0:
            print('Empty tree')
        else:
            self._print_tree(self.root)

    def _print_tree(self, node):
        # 中序遍历
        if node:
            self._print_tree(node.left)
            print(node.data)
            self._print_tree(node.right)
