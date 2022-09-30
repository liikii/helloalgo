#### singly linked list
```
对比数组
不用预定内存。 插入元素不需要像数组一样移动别的元素。 指针实现。 
插入删除便捷， 查找不方便。 没有下标检索。
```


#### doubly linked list
```
有指向前和指向后的指针， 方法向前向后查找。 
```


#### circular list
```
头尾相连，循环检索
```


#### skip list
```
主要是优化排序链表的查找 
如果是排好序的List, 无法使用二分查找。 引入跳跃指针。 
链高度随机决定。 维护理想高度结构太麻烦。 
insert 依赖查找时候的层级前后文关系， 做多级索引。 
del的时候，依赖本元素的前后指针做改变。 
```



#### self-organizing list
```
优化链表查找， 动态元素前移（依赖一些特征）。 比如被查，
```



#### sparse table
```
链表实现， 减少空间浪费
```


#### stack
```
后进先出
数组 链表实现
函数调用关系
```



#### queues
```
数组实现， 用一个head, last指针。 
链表实现。 
```


#### priority queue
```
j.o.hendriksen
链表加优先级指针实现
```


#### recurion
```
一个基， 基于基的后继产生方式
```


#### tail recursion
```
尾递归只是一个变形的循环。 可以用循环实现。 
```



#### nontail recursion
```
非尾递归， 中间状态需要维护。
```


#### indirect recursion
```
间接递归
间接调用自身。 
```



#### nested recursion
```
???
```


#### excessive recursion
```
不合理递归 ， 如fib. 存在重复计算。 
```


#### backtracking
```
八皇后问题
类似对态优化
```



#### binary tree
```
二叉树  数据分层结构， 优化搜索
The formal recursive definition is: a binary tree is either empty (represented by a null pointer), or is made of a single node, where the left and right pointers (recursive definition ahead) each point to a binary tree.

二叉树的实现， 数组把从上到下从左到右的对结构一维化。 
通过类实现，用包含左右的指针实现。  
```



#### breadth-first traversal
```
递归访问， 访问自身， 访问左， 访问右。 从上到下， 从左到历
递归实现， 注意栈空间。 
```


#### depth-first travelsal
```
递归到底， 然后反弹回来。 根据顺序分类， 前中后序。 
递归实现用运行时栈， 非递归实现用用户栈。 效率不高。 
反递归信息写到树里， 解决递归的问题。 
```


#### threaded trees
```
把递归的信息写到树里。 解决递归调用栈的问题。
```



#### joseph m.morris algo
```
???
通过树的转换进行遍历。 
```


#### binary tree insert delete
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


#### tree balance
```
树不平衡， 没有意义
最简单， 是重排， 取中间， 二分。 
```


#### DSW算法
```
把树变链表， 然后再就成平衡树。
```



#### AVL tree  (named after inventors Adelson-Velsky and Landis) 
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


#### 2–3 tree
```
insert 三种情况. 
* To insert into a 2-node
* To insert into a 3-node:
	* If the target node is a 3-node whose parent is a 2-node, the key is inserted into the 3-node to create a temporary 4-node. In the illustration, the key 10 is inserted into the 2-node with 6 and 9. The middle key is 9, and is promoted to the parent 2-node. This leaves a 3-node of 6 and 10, which is split to be two 2-nodes held as children of the parent 3-node.

	* If the target node is a 3-node and the parent is a 3-node, a temporary 4-node is created then split as above. This process continues up the tree to the root. If the root must be split, then the process of a single 3-node is followed: a temporary 4-node root is split into three 2-nodes, one of which is considered to be the root. This operation grows the height of the tree by one. 
```


#### self-adjusting tree
```
树的平衡是不是目的, 目的是找到要找的元素. 
自底向顶旋转
```

#### self-restructing tree
```
单一旋转:把子节点和他的父节点旋转
转动到根部:重复单一旋转, 直到根部. 
```


#### splaying: splay tree 
```
A splay tree is a binary search tree with the additional property that recently accessed elements are quick to access again.
尽管理论上, 自适应树与AVL树界限相当, 但试验表明, AVL树总是比自适应树好. 
```

#### heap