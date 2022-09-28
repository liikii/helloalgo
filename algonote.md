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

