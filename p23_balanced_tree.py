#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen


"""
1、平衡二叉树

概念：平衡二叉树是基于二分法的策略提高数据的查询速度的二叉树的数据结构；

特点：平衡二叉树是采用二分法思维把数据按规则组装成一个树形结构的数据，用这个树形结构的数据
减少无关数据的检索，大大提升了数据检索的速度；

平衡二叉树的数据结构组装过程有以下规则：
（1）非叶子结点只能允许最多两个子结点存在；
（2）每一个非叶子结点数据分布规则为左子结点小于当前结点的值，右子结点大于当前结点的值；

平衡二叉树的层级关系：
因为平衡二叉树查询性能和树的层级（高度h）成反比，h值越小，查询越快，为了保证树的结构左右两端
数据大致平衡，降低二叉树的查询难度，一般会采用一种算法机制实现结点数据结构的平衡，实现了这种
算法的有比如Treap、红黑树，使用二叉平衡树能保证数据的左右两边的结点层级相差不会大于1，通过这
样避免树形结构由于删除增加变成线性链表影响查询的效率，保证数据平衡的情况下，查找数据的速度近似
于二分查找法；

总结二叉平衡树的特点：
（1）非叶子结点最多拥有两个子结点；
（2）非叶子结点值大于左边子结点、小于右边子结点；
（3）树的两边的层级数量差不会大于1；
（4）没有值相等重复的结点；


2、B树

概念：B树和平衡二叉树稍有不同的是B树属于多叉树，又名平衡多路查找树（查找路径不止两条），数据库
索引技术里大量使用的B树和B+树的数据结构；

规则
（1）排序方式：所有结点关键字是按递增次序排序，并遵循左小右大原则；
（2）子结点数：非叶子结点的子结点数>1，且<=2，空树除外（注：M阶代表一个树结点最多有多少个查找
路径，M=M路，当M=2，则是2叉树，当M=3，则是3叉树）；
（3）关键字数：枝结点的关键字数量大于等于ceil/(m/2)-1个且小于等于M-1个（注：ceil()是个朝正无
穷方向取整的函数，如ceil(1.1)的结果是2）；
（4）所有叶子结点均在同一层、叶子结点除了包含关键字和关键字记录的指针外，也有指向其子结点的指针，
只不过其指针都为null；

3、B+树

概念：B+树是B树的一个升级版，相对于B树来说，B+树更充分的利用了结点的空间，让查询速度更稳定，其速
度完全接近于二分查找；

规则：
（1）B+树跟B树不同，B+树的非叶子结点不保存关键字记录的指针，只进行数据索引，这使得B+树每个非叶子
结点所能保存的关键字大大增加；
（2）B+树叶子结点保存了父结点的所有关键字记录的指针，所有数据地址必须要到叶子结点才能获取到。所以
每次查询数据的次数都是一样；
（3）B+树叶子结点的关键字从小到大有序排列，左边结尾数据都会保存右边结点开始数据的指针；
（4）非叶子结点的子结点数=关键字数（来源于百度百科），另一种为非叶子结点的关键字数=子结点数-1（来
源维基百科），虽然两者数据排列结构不一样，但原理还是一样的，MySQL的B+树是用第一种方式实现的；

特点：
（1）B+树的层级更少：相较于B树，B+树每个非叶子结存储的关键字更多，树的层级更少，所以查询速度更快；
（2）B+树查询速度更稳定：B+树所有关键字数据地址都存在叶子结点上，所以每次查找的次数都相同，所以查
询速度要比B树更稳定；
（3）B+树天然具备排序功能：B+树所有的叶子结点数据构成了一个有序链表，在查询大小区间的数据时候更方
便，数据机敏性很高，缓存的命中率也会比B树高；
（4）B+树全结点遍历更快：B+树遍历整棵树只需要遍历所有叶子结点即可，而不需要向B树一样需要对每一层进
行遍历，这有利于数据库做全表扫描；

B树相对于B+树的优点：如果经常访问的数据离根结点很近，而B树的非叶子结点本身存有关键字其数据的地址，
所以这种数据检索的时候会比B+树快；

4、B*树

规则：
B*树是B+树的变种，相对于B+树，它们的不同之处是：
（1）首先是关键字个数限制问题，B+树关键字初始化个数是ceil(m/2),B*树的初始化个数为ceil(2/3*m);
（2）B+树结点满时就会分裂，而B*树结点满时会检查兄弟结点是否满（因为每个结点都有指向兄弟的指针），
如果兄弟结点未满，则向兄弟结点转移关键字，如果兄弟结点已满，则从当前结点和兄弟结点各拿出1/3的数据创
建一个新的结点出来；

特点：
在B+树的基础上，因其初始化的容量大，使得结点空间使用率更高，而又存有兄弟结点的指针，可以向兄弟结点
转移关键字的特性使得B*树的分解次数变得更少；

5、总结
（1）相同的思想和策略：总体来看，平衡二叉树、B树、B+树、B*树贯彻的思想是相同的，都是采用二分法和数据
平衡策略来提升查找数据的速度；
（2）不同方式的磁盘空间利用：不同点是，它们一个一个在演变过程中，通过IO从磁盘中读取数据的原理进行一步
一步的演变，每一次演变都是为了让结点的空间更合理的运用起来，从而是树的层级减少达到快速数据的目的；
"""
