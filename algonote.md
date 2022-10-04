## singly linked list
```
对比数组
不用预定内存。 插入元素不需要像数组一样移动别的元素。 指针实现。 
插入删除便捷， 查找不方便。 没有下标检索。
```


## doubly linked list
```
有指向前和指向后的指针， 方法向前向后查找。 
```


## circular list
```
头尾相连，循环检索
```


## skip list
```
主要是优化排序链表的查找 
如果是排好序的List, 无法使用二分查找。 引入跳跃指针。 
链高度随机决定。 维护理想高度结构太麻烦。 
insert 依赖查找时候的层级前后文关系， 做多级索引。 
del的时候，依赖本元素的前后指针做改变。 
```



## self-organizing list
```
优化链表查找， 动态元素前移（依赖一些特征）。 比如被查，
```



## sparse table
```
链表实现， 减少空间浪费
```


## stack
```
后进先出
数组 链表实现
函数调用关系
```



## queues
```
数组实现， 用一个head, last指针。 
链表实现。 
```


## priority queue
```
j.o.hendriksen
链表加优先级指针实现
```


## recurion
```
一个基， 基于基的后继产生方式
```


## tail recursion
```
尾递归只是一个变形的循环。 可以用循环实现。 
```



## nontail recursion
```
非尾递归， 中间状态需要维护。
```


## indirect recursion
```
间接递归
间接调用自身。 
```



## nested recursion
```
???
```


## excessive recursion
```
不合理递归 ， 如fib. 存在重复计算。 
```


## backtracking
```
八皇后问题
类似对态优化
```



## binary tree
```
二叉树  数据分层结构， 优化搜索
The formal recursive definition is: a binary tree is either empty (represented by a null pointer), or is made of a single node, where the left and right pointers (recursive definition ahead) each point to a binary tree.

二叉树的实现， 数组把从上到下从左到右的对结构一维化。 
通过类实现，用包含左右的指针实现。  
```



## breadth-first traversal
```
递归访问， 访问自身， 访问左， 访问右。 从上到下， 从左到历
递归实现， 注意栈空间。 
```


## depth-first travelsal
```
递归到底， 然后反弹回来。 根据顺序分类， 前中后序。 
递归实现用运行时栈， 非递归实现用用户栈。 效率不高。 
反递归信息写到树里， 解决递归的问题。 
```


## threaded trees
```
把递归的信息写到树里。 解决递归调用栈的问题。
```



## joseph m.morris algo
```
???
通过树的转换进行遍历。 
```


## binary tree insert delete
```
insert 类似search
delete 分情况处理
	is not in a tree;
	is a leaf;
	has only one child;
	has two children.
Deletion starategy is the following: replace the node being deleted with the largest node in the left subtree and then delete that largest node.

If toDelete is not in the tree, there is nothing to delete. If toDelete node has only one child the procedure of deletion is identical to deleting a node from a linked list - we just bypass that node being deleted

Deletion of an internal node with two children is less straightforward. If we delete such a node, we split a tree into two subtrees and therefore, some children of the internal node won't be accessible after deletion. In the picture below we delete 8:
```


## tree balance
```
树不平衡， 没有意义
最简单， 是重排， 取中间， 二分。 
```


## DSW算法
```
把树变链表， 然后再就成平衡树。
```



## AVL tree  (named after inventors Adelson-Velsky and Landis) 
```
insert: 
四种情况， 两种不用处理． 其它两种处理．类似三种. 
If the balance factor of any node in an AVL tree becomes less than –1 or greater 
than 1, the tree has to be balanced. An AVL tree can become out of balance in four 
situations, but only two of them need to be analyzed; the remaining two are symmetrical. The first case, the result of inserting a node in the right subtree of the right 
child. 比如右节点的右节点加元素, 把父元素向上提, 
The second case, the result of inserting a node in the left subtree of the right 
child, is more complex. 先旋转成第一种情况, 再旋转.  
```


## 2–3 tree
```
insert 三种情况. 
* To insert into a 2-node
* To insert into a 3-node:
	* If the target node is a 3-node whose parent is a 2-node, the key is inserted into the 3-node to create a temporary 4-node. In the illustration, the key 10 is inserted into the 2-node with 6 and 9. The middle key is 9, and is promoted to the parent 2-node. This leaves a 3-node of 6 and 10, which is split to be two 2-nodes held as children of the parent 3-node.

	* If the target node is a 3-node and the parent is a 3-node, a temporary 4-node is created then split as above. This process continues up the tree to the root. If the root must be split, then the process of a single 3-node is followed: a temporary 4-node root is split into three 2-nodes, one of which is considered to be the root. This operation grows the height of the tree by one. 
```


## self-adjusting tree
```
树的平衡是不是目的, 目的是找到要找的元素. 
自底向顶旋转
```

## self-restructing tree
```
单一旋转:把子节点和他的父节点旋转
转动到根部:重复单一旋转, 直到根部. 
```


## splaying: splay tree 
```
A splay tree is a binary search tree with the additional property that recently accessed elements are quick to access again.
尽管理论上, 自适应树与AVL树界限相当, 但试验表明, AVL树总是比自适应树好. 
```

## heap
```
Insert
The new element is initially appended to the end of the heap (as the last element of the array). The heap property is repaired by comparing the added element with its parent and moving the added element up a level (swapping positions with the parent). This process is called "percolation up". The comparison is repeated until the parent is larger than or equal to the percolating element.
先把元素插入到最后, 然后把元素推上去. 
DeleteMin
The minimum element can be found at the root, which is the first element of the array. We remove the root and replace it with the last element of the heap and then restore the heap property by percolating down. Similar to insertion, the worst-case runtime is O{log n).
```



## heap sort 
```
The algorithm runs in two steps. Given an array of data, first, we build a heap and then turn it into a sorted list by calling deleteMin. The running time of the algorithm is O(n log n).
把数组当在堆. 建最大堆. 把大元素移到最后, 剩下元素继续建最大堆. 重复. 
```


##  heaps as priority queues.
```
heaps insert:
heapEnqueue(el)
	put el at the end of heap;
	while el is not in the root and el > parent(el)
		swap el with its parent

heap delete:
heapDequeue()
	extract the element from the root;
	put the element from the last leaf in its place;
	remove the last leaf;
	// both subtrees of the root are heaps;
	p = the root;
	while p is not a leaf and p < any of its children
		swap p with the larger child;
```



## organizing array as heap
```
数组实现堆, 最常用实现. 堆就是数组. 数据加堆算法. 
```


## treap
```
用随机堆因子, 使树不至于太失衡. 
randomized binary search tree
tree + heap
 the treap and the randomized binary search tree are two closely related forms of binary search tree data structures that maintain a dynamic set of ordered keys and allow binary searches among the keys. After any sequence of insertions and deletions of keys, the shape of the tree is a random variable with the same probability distribution as a random binary tree; in particular, with high probability its height is proportional to the logarithm of the number of keys, so that each search, insertion, or deletion operation takes logarithmic time to perform.
insert
To insert a new key x into the treap, generate a random priority y for x. Binary search for x in the tree, and create a new node at the leaf position where the binary search determines a node for x should exist. Then, as long as x is not the root of the tree and has a larger priority number than its parent z, perform a tree rotation that reverses the parent-child relation between x and z.
To delete a node x from the treap, if x is a leaf of the tree, simply remove it. If x has a single child z, remove x from the tree and make z be the child of the parent of x (or make z the root of the tree if x had no parent). Finally, if x has two children, swap its position in the tree with the position of its immediate successor z in the sorted order, resulting in one of the previous cases. In this final case, the swap may violate the heap-ordering property for z, so additional rotations may need to be performed to restore this property.
insert 先以二叉插入元素, 然后依堆调整树结构. 
```



## kd tree k-dimensional tree. 
```
把空间分隔. 
以x轴分再用y用, 再用x分. 
```


## polish Notation and Expression Trees
```
???
```


# multiway trees
```
a multiway tree of order m, or an m-way tree
1. Each node has m children and m – 1 keys.
2. The keys in each node are in ascending order.
3. The keys in the first i children are smaller than the ith key.
4. The keys in the last m – i children are larger than the ith ke
```


## b trees
```
一是解决磁盘问题
B-tree is a self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time. The B-tree generalizes the binary search tree, allowing for nodes with more than two children. Unlike other self-balancing binary search trees, the B-tree is well suited for storage systems that read and write relatively large blocks of data, such as databases and file systems.

Bayer and McCreight never explained what, if anything, the B stands for: Boeing, balanced, broad, bushy, and Bayer have been suggested. McCreight has said that "the more you think about what the B in B-trees means, the better you understand B-trees."


definition
* Every node has at most m children.
* Every internal node has at least ⌈m/2⌉ children.
* Every non-leaf node has at least two children.
* All leaves appear on the same level and carry no information.
* A non-leaf node with k children contains k−1 keys.


Insertion and deletion from a B-tree are more complicated; in fact, they are notoriously difficult to implement correctly. For insertion, we first find the appropriate leaf node into which the inserted element falls (assuming it is not already in the tree). If there is already room in the node, the new element can be inserted simply. Otherwise the current leaf is already full and must be split into two leaves, one of which acquires the new element. The parent is then updated to contain a new key and child pointer. If the parent is already full, the process ripples upwards, eventually possibly reaching the root. If the root is split into two, then a new root is created with just two children, increasing the height of the tree by one.

definition:
Every path from the root to a leaf has the same length
If a node has n children, it contains n−1 keys.
Every node (except the root) is at least half full
The elements stored in a given subtree all have keys that are between the keys in the parent node on either side of the subtree pointer. (This generalizes the BST invariant.)
The root has at least two children if it is not a leaf.
```


## b* tree
```
减少分层, 节点必须2/3满. 
```


## b+ tree
```
只有叶结点有数据的引用. 
A B+ tree can be viewed as a B-tree in which each node contains only keys (not key–value pairs), and to which an additional level is added at the bottom with linked leaves.

The primary value of a B+ tree is in storing data for efficient retrieval in a block-oriented storage context — in particular, filesystems. This is primarily because unlike binary search trees, B+ trees have very high fanout (number of pointers to child nodes in a node,[1] typically on the order of 100 or more), which reduces the number of I/O operations required to find an element in the tree.
```


## prefix b+ tree
```
前缀索引， 当河南能找表河南省的时候， 去年省字。 
How efficient are prefix B+-trees? Experimental runs indicate that there is almost no difference in the time needed to execute algorithms in B+-trees and simple prefix B+-trees, but prefix B+-trees need 50–100% more time. In terms of disk accesses, there is no difference between these trees in the number of times the disk is accessed for trees of 400 nodes or less. For trees of 400–800 nodes, both simple prefix B+-trees and prefix B+-trees require 20–25% fewer accesses (Bayer and Unterauer 1977). This indicates that simple prefix B+-trees are a viable option, but prefix B+-trees remain largely of theoretical interest
```


## k-d b tree
```
提高kd tree内存效率
root pointer, region pages, point pages. 
???
```


## bit tree
```
把前缀B树做到极致。
A very interesting approach is, in a sense, taking to the extreme the prefix B+-tree method. In this method, bytes are used to specify separators. In bit-trees, the bit level is reached (Ferguson 1992).
???
```



## R树
```
R: rectangle
从叶子节点开始， 把空间柜起来。 
最小边界矩形
minimal bounding rectangle.
???
```


## 2-4 tree
```
红黑树同构
用B树实现二叉， 但是又会有空间浪费。 引入水平指针， 垂直指针。 双色结构 中称为红指针黑指针。 
???
2–3–4 tree (also called a 2–4 tree) is a self-balancing data structure that can be used to implement dictionaries. The numbers mean a tree where every node with children (internal node) has either two, three, or four child nodes:

a 2-node has one data element, and if internal has two child nodes;
a 3-node has two data elements, and if internal has three child nodes;
a 4-node has three data elements, and if internal has four child nodes;

2–3–4 trees are isomorphic to red–black trees, meaning that they are equivalent data structures. In other words, for every 2–3–4 tree, there exists at least one red–black tree with data elements in the same order. Moreover, insertion and deletion operations on 2–3–4 trees that cause node expansions, splits and merges are equivalent to the color-flipping and rotations in red–black trees.
```


## trie
```
Trie的核心思想是空间换时间。利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。

前缀树的3个基本性质：
* 根节点不包含字符，除根节点外每一个节点都只包含一个字符。
* 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串。
* 每个节点的所有子节点包含的字符都不相同。
???
```



