## books
```
《管理运筹学》关文忠
《c++数据结构与算法》 adam drozdek
```

## stanford courses
```
cs161 algorithms
• CS154 – Introduction to Automata and Complexity
• CS163 – The Practice of Theory Research
• CS166 – Data Structures
• CS168 – The Modern Algorithmic Toolbox
• MS&E 212 – Combinatorial Optimization
• CS250 – Error Correcting Codes
• CS252 – Analysis of Boolean Functions
• CS254 – Computational Complexity
• CS255 – Introduction to Cryptography
• CS259Q – Quantum Computing
• CS260 – Geometry of Polynomials in Algorithm Design
• CS261 – Optimization and Algorithmic Paradigms
• CS263 – Counting and Sampling
• CS265 – Randomized Algorithms
• CS269O – Introduction to Optimization Theory
• MS&E 316 – Discrete Mathematics and Algorithms
• CS352 – Pseudorandomness
• CS366 – Computational Social Choice
• CS368 – Algorithmic Techniques for Big Data
• EE364A/B – Convex Optimization I and II
```


## references
```
Course Contents
Asymptotic Notation, Divide-and-Conquer Paradigm, Recurrences
Sorting Algorithms: Insertion Sort, Merge Sort, Heap Sort, Quick Sort
Sorting Lower Bounds, BucketSort, RadixSort.
Trees, Binary Search Trees, AVL Trees, Red-Black Trees, Treaps
Tries, Compact Tries
Hashing.
String Matching: Knuth-Morris-Pratt Algorithm, Boyer-Moore Algorithm, Aho-Corasick Algorithm
Suffix Trees, Ukkonen’s Algorithm, Suffix Arrays
Dynamic Programming with Samples: Knapsack Problem, Levenshtein Distance (LCS Problem)
Greedy Algorithms with Samples: Huffman Coding, Activity Selection Problem, LCS Problem via Greedy Algorithm
Graphs. Topological Sort, Strongly Connected Components, Minimum Spanning Trees.
Single-Source and All-Pairs Shortest Paths in Graphs. Dijkstra’s Algorithm, Bellman-Ford Algorithm, Floyd-Warshall Algorithm
Maximum Flow, Ford-Fulkerson Method
Introduction to Automata. Deterministic Finite Automata. Nondeterministic Finite Automata
Regular Expressions
Decision and Closure Properties of Regular Languages
Context-Free Languages. Properties of Context-Free Languages
Parse Trees. Normal Forms for Context-Free Grammars
Pushdown Automata. Equivalence of CFG’s and PDA’s
Range Minimum Queries (RMQ).
Cartesian Trees and RMQ.

=============================
Fundamental Data Structures
Introduction
Abstract data type
Data structure
Analysis of algorithms
Amortized analysis
Accounting method
Potential method
Sequences
Array data type
Array data structure
Dynamic array
Linked list
Doubly linked list
Stack (abstract data type)
Queue (abstract data type)
Double-ended queue
Circular buffer
Dictionaries
Associative array
Association list
Hash table
Linear probing
Quadratic probing
Double hashing
Cuckoo hashing
Hopscotch hashing
Hash function
Perfect hash function
Universal hashing
K-independent hashing
Tabulation hashing
Cryptographic hash function
Sets
Set (abstract data type)
Bit array
Bloom filter
MinHash
Disjoint-set data structure
Partition refinement
Priority queues
Priority queue
Bucket queue
Heap (data structure)
Binary heap
d-ary heap
Binomial heap
Fibonacci heap
Pairing heap
Double-ended priority queue
Soft heap
Successors and neighbors
Binary search algorithm
Binary search tree
Random binary tree
Tree rotation
Self-balancing binary search tree
Treap
AVL tree
Red–black tree
WAVL tree
Scapegoat tree
Splay tree
Tango tree
Skip list
B-tree
B+ tree
Rope
Integer and string searching
Trie
Radix tree
Suffix tree
Suffix array
Suffix automaton
Van Emde Boas tree
Fusion tree

```


## greedy method 
```
最大  最小问题
优化问题
```

## linear programming
```
线性规划
最大  最小问题
feasible solution
feasible region
optimal solution
optimal value
```

## Abdul Bari


## dynamic programming
```
动态规划问题
一个最优策略的子策略总是最优的
```

## branch and bound 
```
整数规划
The algorithm depends on efficient estimation of the lower and upper bounds of regions/branches of the search space. If no bounds are available, the algorithm degenerates to an exhaustive search.
```


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



# graph
```
顶点与顶点边之间的集合。 
重点动态规划
运筹学 关文忠
```


## graph representation
```
图表示法， 
邻接表示法， 矩阵表示法， 关联矩阵表示法

```


## graph traversals
```
广度  深度
广度:
while
一个个消灭， 再消灭连接的点， 继续
一层层包围式。 
深度:
per-order recursion
发现一个往下就往下递归。 最小树。 spanning tree. 
```


## shortest paths
```
马车驿站问题
倒序想， 找边界最近点。 
找边界最近点
增广动态优化
```


## all to all shortest path problem
```
矩阵算法
增广
```

## cycle detection  
```
wfi 矩阵算法可以， 增广0值发生变化 
使用 DFS 可以判断一个无向图和有向中是否存在环。深度优先遍历图，如果在遍历的过程中，发现某个结点有一条边指向已访问过的结点，并且这个已访问过的结点不是上一步访问的结点，则表示存在环。
```

##  union-find problem
```
disjoint set 
例如， 三个点， 两条边 组成了三个点的集合， 加入另一条边， 他不属于已有的边， 但是他的两个点在原集合。 证明有个环。 
```



## minimal spanning tree
```
避圈法（找最短边）
任选一结点 放入集合V， 其余结点放入集合W。 
找出集合之间最短的边， 然后把最短连接点放入集合V。 
破圈法（）
```


## Connectivity 
```
dfs 
```

## connectivity in undirected graphs
```
dfs 
???
```

## connectivity in directed graphs
```
dfs
???
```



## topological Sort
```
applications:
* build systems
* advanced-packaging tool(apt-get)
* task scheduling
* pre-requisite problems
动态优化， 找出最不依赖的元素， 删了， 然后再找。 
```


# networks
## maximum flows
```
最大流问题， 最大运输量问题
流量容量
先找一条可行路径为增长链
从S-T找到一条最大流。然后再找一条， 直到没有
```


## maximum flows of minimum cost
```
最小费用最大流
线性规划法
图解法
分出两张图， 一个流量图， 一个费用图。 
费用图的最短路  流量不够用动态优化
```


## matching 
```
婚姻问题
完美匹配  不稳定匹配  稳定匹配
动态优化问题
findmaximummatching 
stable matching problem
assignment problem
```


## matching in nonbipartite graph
```
二分图  男女图
非二分图
```

## eulerian and hamiltonian graph
## eulerian graphs
```
七桥问题
中国邮递员问题（奇点最多重复一次）
奇点之间组成回路
```

## graph coloring 
```
???
```

# np-complete problems in graph
## the clique problem
```
派系问题
```

## the 3-colorability problem
```
三色问题 四色可以分所有图
```


## the vertex cover problem
```
顶点覆盖问题
图的覆盖是一個顶点的集合，使图中的每一条边都至少連結該集合中的一个顶点。寻找最小的顶点覆盖的问题称为顶点覆盖问题（Vertex cover），它是一个NP完全问题。
网点问题
```


## the hamiltonian cycle problem
```
???
```


## sorting
```
... ...
```

## insertion sortting
```
把数组 看成虚拟的两个数组， 一个数组为空。 然后插入到他的位置。
类似接牌， 从第一张开始比。 
多余对比
```


## selection sortting
```
先找最小， 然后找次小
多余对比
```


## buble sort
```
从头开始向下， 一对一对比，比出最大到最后。 然后再来一轮找二大。  
```


## comb sort 
```
Comb sort improves on bubble sort in the same way that Shellsort improves on insertion sort.
The basic idea is to eliminate turtles, or small values near the end of the list, since in a bubble sort these slow the sorting down tremendously. Rabbits, large values around the beginning of the list, do not pose a problem in bubble sort.
```


## decison trees
```
???
```


## efficient sorting algorithms
```
先对原始数组的各部分进行排序， 待各个部分已有序时， 再对整个数组排序
```
## shell sort
```
shell对插入的改进。 类似跳表。 
减少冒泡与插入排序的极端情况
a generalization of sorting by exchange (bubble sort) or sorting by insertion (insertion sort).
The running time of Shellsort is heavily dependent on the gap sequence it uses. For many practical variants, determining their time complexity remains an open problem.
？？
```


## heap sort
```
把数据看成一个堆
最小堆最大堆
In computer science, heapsort is a comparison-based sorting algorithm. Heapsort can be thought of as an improved selection sort: like selection sort, heapsort divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element from it and inserting it into the sorted region. Unlike selection sort, heapsort does not waste time with a linear-time scan of the unsorted region; rather, heap sort maintains the unsorted region in a heap data structure to more quickly find the largest element in each step
```


## quick sort
```
分治  取中位数， 分类， 然后  
Quicksort is an in-place sorting algorithm. Developed by British computer scientist Tony Hoare in 1959[1] and published in 1961,[2] it is still a commonly used algorithm for sorting. When implemented well, it can be somewhat faster than merge sort and about two or three times faster than heapsort.
```


## merge sort
```
合并已排好序的小数组。
The problem with quicksort is that its complexity in the worst case is O(n2
) because it is difficult to control the partitioning process. Different methods of choosing a bound attempt to make the behavior of this process fairly regular; however, there is no guarantee that partitioning results in arrays of approximately the same size. Another strategy is to make partitioning as simple as possible and concentrate on merging the two sorted arrays. This strategy is characteristic of mergesort. It was one of the first sorting algorithms used on a computer and was developed by John von Neumann
```


## radix sort
```
基数排序
个位数排好， 十位数排， 十位数排好， 百位数排。 

```


## counting sort 
```
找出数据最大数， 做成数组， 然后各找出各的位置。 命中计数加1（主要解决一个数出现多次问题）， 把数组从头到尾叠加。 就是想应元素的位置。 
计数排序缺点空间浪费。 
```



# hashing
```
快速得到要查找元素的index.
key space ---> hash table
表索引 One to one. 
hash 索引  many to one
```

## hash functions
```
... ...
```

## division
```
取模
```


## folding
```
A folding hash code is produced by dividing the input into n sections of m bits, where 2m is the table size, and using a parity-preserving bitwise operation such as ADD or XOR to combine the sections, followed by a mask or shifts to trim off any excess bits at the high or low end. For example, for a table size of 15 bits and key value of 0x0123456789ABCDEF, there are five sections consisting of 0x4DEF, 0x1357, 0x159E, 0x091A and 0x8. Adding, we obtain 0x7AA4, a 15-bit value.
```



## Mid-squares
```
平方取中
A mid-squares hash code is produced by squaring the input and extracting an appropriate number of middle digits or bits. For example, if the input is 123,456,789 and the hash table size 10,000, squaring the key produces 15,241,578,750,190,521, so the hash code is taken as the middle 4 digits of the 17-digit number (ignoring the high digit) 8750. The mid-squares method produces a reasonable hash code if there is not a lot of leading or trailing zeros in the key. This is a variant of multiplicative hashing, but not as good because an arbitrary key is not a good multiplier.
```


## Extraction
```
只取部分关键字来计算
```


## radix transformaion
```
基数转换法
Using the radix transformation, the key K is transformed into another number base; 
K is expressed in a numerical system using a different radix. If K is the decimal number 345, then its value in base 9 (nonal) is 423. This value is then divided modulo 
TSize, 
```

## Universal Hash Functions
```
全域散列法
？？？
全域哈希指的是在哈希函数中, 加入随机值保证哈希函数的不同. 用于实现完美散列, 其中各表随机值是要保存的.
```

## collision resolution
```
几乎所有的散列函数都会出现多个关键字同时映射到一个位置的情况。 
```

## open addressing
```
持续在hashtable里找新（空）位置， 线性探查， linear probe.
以不同间隔找新位置
Open addressing, or closed hashing, is a method of collision resolution in hash tables. With this method a hash collision is resolved by probing, or searching through alternative locations in the array (the probe sequence) until either the target record is found, or an unused array slot is found, which indicates that there is no such key in the table.[1] Well-known probe sequences include:
* Linear probing
in which the interval between probes is fixed—often set to 1.
* Quadratic probing
平方加入。 
in which the interval between probes increases quadratically (hence, the indices are described by a quadratic function).
* Double hashing
in which the interval between probes is fixed for each record but is computed by another hash function.

Some open addressing methods, such as Hopscotch hashing, Robin Hood hashing, last-come-first-served hashing and cuckoo hashing move existing keys around in the array to make room for the new key. This gives better maximum search times than the methods based on probing. 
```


## chainging 
```
* separate chaining: 
hashtalbe表里的每个位置存放着一个链表
Keys do not have to be stored in the table itself. In chaining, each position of the table 
is associated with a linked list or chain of structures whose info fields store keys or 
references to keys.


* coalesced hashing
hashtable存放值和next Pointer(linear probe)
Coalesced hashing, also called coalesced chaining, is a strategy of collision resolution in a hash table that forms a hybrid of separate chaining and open addressing.
. Noncolliding keys are 
stored in their home positions, as in Figure 10.7a. Colliding keys are put in the last 
available slot of the cellar and added to the list starting from their home position
```


## Bucket Addressing
```
把冲突的元素放在表中同一个段位置， 然后再设一个溢出区。 
```


## deletion
```
线性探查法， 删除， 标记式删除。 为了后期的探查 。 表在删除记录达到一定数量后，进行清洗。 
```

## perfect hash function
```
In computer science, a perfect hash function h for a set S is a hash function that maps distinct elements in S to a set of m integers, with no collisions. In mathematical terms, it is an injective function.
Algorithms for constructing perfect hash functions tend to be tedious, but a number are
known.
```

## Cichelli’s Method
```
One algorithm to construct a minimal perfect hash function was developed by Richard 
J. Cichelli. It is used to hash a relatively small number of reserved words. The function 
is of the formh(word) = (length(word) + g(firstletter(word)) + g(lastletter(word))) mod TSize
```

## The FHCD Algorithm
```
...
```


## rehashing
```
```


## cockoo hashing
```
两个hash function, two hashtable, 空位置就插入， 不空驱逐旧的， 放下一个表。 
● To insert an element x,
start by inserting it
into table 1.
● If h₁(x) is empty, place
x there.
● Otherwise, place x
there, evict the old
element y, and try
placing y into table 2.
● Repeat this process,
bouncing between
tables, until all
elements stabilize.
```



## hash functions for extendible files
```
再散列需要花太多时间， 创建出了另一种散列方法。 减少rehash时间。 
In the directory schemes, key access is mediated by the access to a directory or 
an index of keys in the structure. There are several techniques and modifications to 
those techniques in the category of the directory schemes. We mention only a few: 
expandable hashing (Knott 1971), dynamic hashing (Larson 1978), and extendible 
hashing (Fagin et al. 1979). 
```


## Hash Functions for Extendible Files
```
LSB:最后字节为目录， 一开始设为1位， 如果bucket溢出，设成二位， 然后对溢出的重整。 比如01， 11没溢出， 没溢出的还指向过去的桶。 
Hash Functions for Extendible Files
目录：这些容器存储指向存储桶的指针。每个目录都有一个唯一的ID，该ID在每次扩展时都会更改。哈希函数返回此目录ID，该目录ID用于导航到相应的存储桶。目录数= 2 ^全球深度。
存储桶：存储散列密钥。目录指向存储桶。如果存储桶的局部深度小于全局深度，则该存储桶可能包含多个指向它的指针。
全局深度：它与目录相关联。它们表示哈希函数用来对密钥进行分类的位数。全局深度=目录ID中的位数。
Local Depth：与Local Depth相同，除了Local Depth与存储桶(而不是目录)相关联这一事实。根据全局深度的局部深度用于确定在发生溢出的情况下要执行的操作。局部深度始终小于或等于全局深度。
存储桶拆分：当存储桶中的元素数量超过特定大小时，该存储桶将分为两部分。
目录扩展：当存储桶溢出时，将进行目录扩展。当溢出存储桶的本地深度等于全局深度时，将执行目录扩展。

步骤1 –分析数据元素：数据元素可能以各种形式存在，例如整数，字符串，浮点数等。当前，让我们考虑整数类型的数据元素。例如：49。
步骤2 –转换为二进制格式：将数据元素转换为二进制格式。对于字符串元素，请考虑起始字符的ASCII等效整数，然后将其转换为二进制形式。由于我们有49个数据元素，因此其二进制格式为110001。
步骤3 –检查目录的全局深度。假设哈希目录的全局深度为3。
步骤4 –识别目录：考虑二进制数中LSB的“全球深度”数，并将其与目录ID匹配。
例如。得到的二进制文件：110001和全球深度为3。因此，哈希函数会返回110 001即3个LSB。 001。
第5步–导航：现在，导航到目录ID为001的目录所指向的存储桶。
步骤6 –插入和溢出检查：插入元素并检查存储桶是否溢出。如果遇到溢出，请执行步骤7，然后执行步骤8 ，否则，请执行步骤9 。
步骤7 –在数据插入过程中解决流状况：很多时候，将数据插入存储桶时，可能会发生存储桶溢出的情况。在这种情况下，我们需要遵循适当的程序以避免数据处理不当。
首先，检查局部深度是否小于或等于整体深度。然后选择以下情况之一。
情况1：如果溢出的存储桶的局部深度等于全局深度，则需要执行目录扩展以及存储桶拆分。然后将全局深度和局部深度值加1。然后，分配适当的指针。
目录扩展将使哈希结构中存在的目录数量增加一倍。
情况2：如果局部深度小于整体深度，则仅发生“桶分割”。然后仅将本地深度值加1。然后，分配适当的指针。

第8步-重新分割拆分存储区元素：拆分后的溢出存储区中存在的元素将通过目录的新全局深度进行重新整理。
步骤9 –元素成功散列。
```

## dynamic hashing
```
dynamic hashing
```


## linear hashing
```
线性散列
比如 初始化 tsize=4, h0 = Hash function to be used h0(K) = K mod  1 * 4.  1=2的零次方. split pointer = 0.  round = 0.
如果一个溢出， 启动线性散列后继h1  h1(K) = K mod 2 * 4. 2 = 2的1次方。 然后再线性加一个bucket.然后重新Hash split split pointer指的桶。 上移split pointer. 
tsize 都split完。 round += 1. split reset 复位到0。 基础hash 设为h1, 后继hash设为h2. 
====================================================================================
查找的时候。 
根据split值，和tsize值， round值， 决定那些部分用当前hash function. 那些用后继函数来查找。 



One-line summary: Linear hashing is a hashing scheme that exhibits near-optimal performance, both in terms of access cost and storage load.
Hashing basics:
records indexed with primary (unique) key
hashing function h(c) assigns to a key c a unique bucket.
If a bucket becomes full, we have a collision. Collision resolution is the process of storing c (which is now an overflow record) into an overflow bucket. Chaining is the usual way of doing it.
Instead of chaining or overflow bucket creation, it would be nice to reorganize data or add more buckets, both of which require a dynamically created hash function, which is usually a modification to the currently used hash function, called a split.
===================================================================================
AN EXAMPLE
This example shows various aspects of linear hashing with more data. Initially the file (at least logically) will be empty. As records are inserted into the file, buckets are added to the file. Key of each record could consist of one or more fields of the record. We assume that a hash function is used to come up with a number before hashing function specified in the linear hashing is used.

Let each bucket has capacity for storing 4 records.

Let initial number of buckets N be 4.

Record key values could be numbers, names or a combination of these depending on fields you select as key for the file. If a key contains more than one field or a key field is not a number, we have to use a hash function to get a number because we are going to use other hash functions to map record keys to bucket numbers.

Note:- The example is directly taken from third edition of the book Database Management Systems by Ramakrishnan and Gehrke.
3.1 INSERTING RECORDS
1) Insert record with keys 32, 44, 36, 9, 25, 5, 14, 18, 10, 30, 31, 35, 7 and 11

Current round i = 0.
Split pointer s = 0.
Hash function to be used h0(K) = K mod 4.
h0(32) = 32 mod 4 = 0. Insert record in bucket 0.
h0(44) = 44 mod 4 = 0. Insert record in bucket 0.

2) Insert record with key 43.

Current round i = 0.
Hash function to be used h0(K) = K mod 4
h0(43) = 43 mod 4 = 3. Insert record in bucket 3. But the bucket is full.
Add an overflow page and chain it to 3.
Because there is an overflow, split bucket 0 pointed to by s and add a new bucket 4.
Redistribute bucket 0 contents between buckets 0 and 4 using next hash function h1(K) = K mod 2 * 4.
Increment split pointer.

3) Insert record with key 37.

Current round i = 0.
Hash function to be used h0(K) = K mod 4
h0(37) = 37 mod 4 = 1. Insert record in bucket 1.


4) Insert record with key 29.

Current round i = 0.
Hash function to be used h0(K) = K mod 4
h0(29) = 29 mod 4 = 1. Insert record in bucket 1. But the bucket is full.
Split bucket 1 pointed to by s.
Add new bucket 5.
Redistribute bucket 1 contents and 29 between buckets 1 and 5 with new hash function h1(K) = K mod 2 * 4.
Increment split pointer
No overflow page is needed because we are splitting the same bucket to which the key was mapped with the original hash function.


5) Insert record with key 22.

Current round i = 0.
Hash function to be used h0 (K) = K mod 4.
h0 (22) = 22 mod 4 = 2. Insert record in bucket 2. But the bucket is full.
Split bucket 2 pointed to by s.
Add new bucket 6.
Redistribute bucket 2 contents and 22 between buckets 2 and 6 with new hash function h1(K) = K mod 2 * 4.
Increment split pointer
No overflow page is needed because we are splitting the same bucket to which the key was mapped with the original hash function.


6) Insert record with key 66.

Current round i = 0.
Hash function to be used h0(K) = K mod 4
h0(66) = 66 mod 4 = 2. Insert record in bucket 2.
Since 2 < s, we have to use h1 hash function.
h1(66) = 66 mod 8 = 2. The same bucket number and hence insert record in bucket 2.

7) Insert record with key 34.

Current round i = 0.
Hash function to be used h0(K) = K mod 4
h0(34) = 34 mod 4 = 2. Insert record in bucket 2.
2 < s, hence need to use h1 hash function.
h1(34) = 34 mod 8 = 2. Again the same bucket. Insert record in bucket 2.

8) Insert record with key 50.

Current round i = 0.
Hash function to be used h0(K) = K mod 4
h0(50) = 50 mod 4 = 2. Insert record in bucket 2.
As 2 < s, use h1 for hashing.
h1(50) = 50 mod 8 = 2. The same bucket. Insert record in bucket 2.
But the bucket is full.
Split bucket 3.
Add new bucket 7.
Redistribute bucket 3 contents and 50 between buckets 2 and 7 with new hash function h1(K) = K mod 2 * 4.
Add an overflow bucket, insert 50 in it and chain it to bucket 2
Increment split pointer. It will be 4.
Since it is equivalent to initial number of buckets N = 4, reset it to 0.
Use has function to be used as h1(K) = K mod 2 * 4 for further insertion of records.
Set next round i to i + 1. Now the round i will be 1.


9) Insert record with key 45.

Current round i = 1.
Hash function to be used h1(K) = K mod 2 * 4.
h1(45) = 45 mod 8 = 5. Insert record in bucket 5.


10) Insert record with key 53.

Current round i = 1.
Hash function to be used h1(K) = K mod 21 * 4
h1(53) = 53 mod 8 = 5. Insert record in bucket 5. But the bucket is full.
Therefore, split bucket 0 as pointed to by split pointer.
Add new bucket 8.
Redistribute its contents between buckets 0 and 8 with new hash function h2(K) = K mod 22 * 4 = K mod 16.
h1(32) = 32 mod 16 = 0. Hence 32 remains in the same bucket
Add an overflow bucket, insert 53 in it and chain it to bucket 5
Increment split pointer. It will be 1.

11) Insert record with key 48, 64, 80

Current round i = 1.
Hash function to be used h1(K) = K mod 21 * 4 = K mod 8.
h1(48) = 48 mod 8 = 0. Insert record in bucket 0.
Since 0 < s, h2(48) = 48 mod 22*4= 48 mod 16 = 0. Insert record in bucket 0.
h1(64) = 64 mod 8= 0. Insert record in bucket 0.
Since 0 < s, h2(64) = 64 mod 22*4= 64 mod 16 = 0. Insert record in bucket 0.
h1(80) = 80 mod 8 = 0. Insert record in bucket 0.
Since 0 < s, h2(80) = 80 mod 22*4= 80 mod 16 = 0. Insert record in bucket 0.


12) Insert record with key 40

Current round i = 1.
Hash function to be used h1(K) = K mod 21 * 4 = K mod 8.
h1(40) = 40 mod 8 = 0.
Since 0 < s, h2(40) = 40 mod 22 * 4 = 40 mod 16 = 8. Insert record in bucket 8.

3.2 SEARCHING
Searching can be done as following. If current hash function is hi(K), let bucket b = hi(K). If b < s, then let b = hi+1(K). Search for the record with K in bucket b.

In the above example, current hash function is h1(K) = K mod 21*4 = K mod 8.

EXAMPLES
SEARCH FOR RECORD WITH KEY 35
Bucket b = 35 mod 8 = 3 and 35 is in bucket 3.

SEARCH FOR RECORD WITH KEY 64
Bucket b = 64 mod 8 = 0. Since 0 < s, b = 64 mod 16 = 0. Again bucket 0 and 64 is in bucket 0.

SEARCH FOR RECORD WITH KEY 40
Bucket b = 40 mod 8 = 0. Since 0 < s, b = 40 mod 16 = 8. 40 is in bucket 8.

SEARCH FOR RECORD WITH KEY 52 (DOES NOT EXIST)
Bucket b = 52 mod 8 = 4. 42 is not in bucket 4 as expected.

4 NOTES
In a round, if a bucket to which a key is hashed is full, buckets are split in the order of bucket numbers 0, 1, 2, 3, etc., irrespective of whether or not the buckets are full.
When a key is hashed to bucket b that is full, bucket pointed to by the split pointer is split and not the bucket b. An overflow page is chained to b or its existing overflow page to accommodate the new key.
In a round, when split pointer is equal to number of buckets present at the beginning of the round, it is reset to 0, a new round is started, buckets are split again starting from bucket 0 and new hash function hi+1(K) is used.
If hashed bucket for key K is less than split pointer bucket, key has to be rehashed using hi+1(K) to know bucket number of the key.
When all initial buckets are split, number of buckets will be double the number of initial buckets.
Number of initial buckets need not be multiple of 2.
```


# Data Compression


## Conditions for Data Compression
```
Conditions for Data Compression
```


## Huffman Coding
```
Huffman Coding
思路 对字符重新编码， 前缀不覆盖， 频率高的用短编码频率低的用长编码。 得预先知道出现频率。 
```


##  Adaptive Huffman Coding
```
解决预先得有词频率的问题， 动态生成Huffman 树， 依赖频率。 
```


## Run-Length Encoding
```
nnnnnn = 6n
```



##  Ziv-Lempel Code  lzw
```
TOBEORNOTTOBEORTOBEORNOT
用短编码代替长字
一次读一个词和他的后继， 然后查字典， 如果没有就在字典里插入这一对， 比如to 27.  no 33 如果有就再读他的后缀not, 编not. 。 
读取的时候
读取的时候， 也是根据读到的字和它的后继建字典， 然后解后边短编的码。 
```



# Memory Management
```
Memory Management
外部碎片
external fragmentation
内部碎片
internal fragmentation
```

## The Sequential-Fit Methods
```
用链表维护， 分配第一个满足的， 分配最接近的， 分配最大的  分配第二个满足的
first-fit best-fit worst-fit next-fit
```


## The Nonsequential-Fit Methods
```
exact fit oldehoeft allan
The Nonsequential-Fit Methods
```



## Buddy Systems
```
Buddy Systems
```


##  Garbage Collection
```
Garbage Collection

Garbage collection methods usually include two phases, which may be implemented as distinct passes or can be integrated:
1.	 The marking phase—to identify all currently used cells.
2. The reclamation phase—when all unmarked cells are returned to the memory pool; 
this phase can also include heap compaction.
垃圾回收一般分两个阶段， 标记阶段。 重新声明阶段。 
```

## Mark-and-Sweep
```
Mark-and-Sweep
Mark and sweep is one of the earliest and best-known garbage collection algorithms.

It works perfectly well with cycles, but
requires some significant support from the compiler and run-time support system.
Assumptions   
The core assumptions of mark and sweep are:

Each object on the heap has a hidden "mark" bit.
We can find all pointers outside the heap (i.e., in the activation stack and static area)
For each data object on the heap, we can find all pointers within that object.
We can iterate over all objects on the heap
 tracing garbage collection is a form of automatic memory management that consists of determining which objects should be deallocated ("garbage collected") by tracing which objects are reachable by a chain of references from certain "root" objects, and considering the rest as "garbage" and collecting them.

 ????


This algorithm actually goes through 3 important steps.
 Root: In general, a root is a global variable that is used in the code. A window object in javascript can act as a   root. This algorithm uses global object root to find whether the objects are reachable or unreachable.
This algorithm then monitors every root and also their children. While monitoring, some objects which are reachable are marked and remaining objects which are unreachable are unmarked, based on the provided conditions.
 The objects which are unmarked, that means which are unreachable will be garbage collected. 


In the presentation we discussed two of the basic garbage collection algorithms:
Mark-Sweep and Mark-Compact. Both algorithms attempt to locate all the live objects in
the memory heap, and free up the memory of all the unmarked objects (the garbage).
Because true liveness is undecidable, pointer reachability is used instead - an object is
deemed live iff it can be reached by following a path from a set of known roots.
Mark-Sweep has two phases: first, we locate and mark all live objects in the heap
(with a DFS from the roots). The marking is done by setting a mark-bit in the header of
an object, or by using a special table - a bitmap. In the second phase, all the heap is
traversed, and the memory occupied by any object that didn’t have its mark-bit set is
freed. Mark-Sweep is very fast and simple, but prone to severe fragmentation problems.
Mark-Compact also has two phases: first, we mark all the live objects, as before.
Then we relocate (move) objects on the heap, with the intention of compacting the heap
so that all the live objects would be located at the beginning of the heap, and all the
memory that comes after those objects will be free for allocation. The most common
and widely used relocation is technique is called sliding - all the live objects are slid to
the beginning of the heap, “squeezing out” the garbage, while retaining their order (and
thus, the spatial locality). Mark-Compact solves the fragmentation problem, usually at
the cost of memory overhead, and longer running time.
My original contribution was the Snapshot algorithm. The idea behind it is the fact
that the set of dead objects doesn’t shrink, so the mutator threads don’t have to be
stopped while garbage collection is performed. Mutators are stopped for a short period,
while a snapshot (a copy) of the relevant part of the heap is taken. That copy is then
traversed to locate all the dead objects. The last step is to traverse the original heap
(possibly concurrently with mutator threads) and free all the objects that were deemed
dead in the copy (because those couldn’t possibly come back to life in the original).
During the discussion after the presentation a couple of improvements to MarkSweep came up:
● Using a FIFO buffer for prefetching objects ahead of time.
● Using edge-marking to reduce the number of cache misses.

```



## copying methods 
```
stop and copy algorithm
旧空间满后， 把有用的移到新空间。 旧空间清空。 
At an abstract level, all a copying collector does is start from a set of roots (in our case, the operand stack), and traverse all of the reachable memory-allocated objects, copying them from one half of memory into the other half. The area of memory that we copy from is called old space and the area of memory that we copy to is called new space. When we copy the reachable data, we compact it so that it is in a contiguous chunk. So, in effect, we squeeze out the holes in memory that the garbage data occupied. After the copy and compaction, we end up with a compacted copy of the data in new space data and a (hopefully) large, contiguous area of memory in new space in which we can quickly and easily allocate new objects. The next time we do garbage collection, the roles of old space and new space will be reversed.


```


## Incremental Garbage Collection
```
* Copying Methods
过去方法调用垃圾回收会占用过多时间
Incremental Garbage Collection
stop-and-copy fromspace topspace
* nonCopying Methods
yuasa algorithms mark sweep
```


## 	 Generational Garbage Collection
```
分代垃圾回收。 
```


# String Matching

##  Exact String Matching
```
从第一个字开始匹配， 如不中， 第二个。 
bruteforcestringmatching
```


## Straightforward Algorithms
```
Exact string matching consists of finding an exact copy of pattern P in text T. It is an 
all-or-nothing approach; if there is a very close similarity between P and a substring of 
T, the partial match is rejected
```


##  The Knuth-Morris-Pratt Algorithm
```
减少多余比较
The Knuth-Morris-Pratt Algorithm
```


## Boyer-Moore Algorithm
```
???
```


## Multiple Searches
```
Multiple Searches
找所有出现的位置
```



## Bit-Oriented Approach
```
神算法
状态转换算法
baezn yates gamnet 算法
bitap算法
shift or shift and 算法
==================================
状态叠加， 状态不清空， 状态不行动， 不重复比较。 

```


##  Matching Sets of Words
```
单词集合的匹配
aho corasick
```

## Regular Expression Matching
```
语言与自动机
An algorithm created by Ken Thompson constructs a nondeterministic finite 
automaton (NDFA) corresponding to a regular expression. 
```

## Suffix Tries and Trees
```
Suffix Tries and Trees
```


##  Suffix Arrays
```
Suffix Arrays
```


## Approximate String Matching
```
Approximate String Matching
edit distance
```

## String Similarity
```
String Similarity
```


##  String Matching with k Errors
```
wu manber matching
String Matching with k Errors
```

## cs166 additional
```

```

## range minimum query
```
找出区间里最小， 2个组合多少对。 然后提前求出。 
a range minimum query (RMQ) solves the problem of finding the minimal value in a sub-array of an array of comparable objects. Range minimum queries have several use cases in computer science, such as the lowest common ancestor problem and the longest common prefix problem (LCP).


Naive solution
In a typical setting, the array A is static, i.e., elements are not inserted or deleted during a series of queries, and the queries to be answered on-line (i.e., the whole set of queries are not known in advance to the algorithm). In this case a suitable preprocessing of the array into a data structure ensures faster query answering. A naïve solution is to precompute all possible queries, i.e. the minimum of all sub-arrays of A, and store these in an array B such that B[i, j] = min(A[i…j]); then a range min query can be solved in constant time by array lookup in B. There are Θ(n²) possible queries for a length-n array, and the answers to these can be computed in Θ(n²) time by dynamic programming.[1]


The Range Minimum Query problem
(RMQ for short) is the following:
Given an array A and two indices i ≤ j, 
what is the smallest element out of
A[i], A[i + 1], …, A[j – 1], A[j]?



There's a simple O(n)-time algorithm for
evaluating RMQA(i, j): just iterate across the
elements between i and j, inclusive, and take
the minimum

● Naïvely precomputing the table is inefficient.
● Can we do better?
● Claim: We can precompute all subarrays in time Θ(n
2
)
using dynamic programming.
最简单算法， 一个个算出来。 遍历。 
第二种算法， 动态规划， 一个个的结果，算两个最小， 两两的最小得三个的最小， 三个个的对比得四个。 依次。 

方法三 Block Decomposition
分成block块。 
方法四  Sparse Tables

```
