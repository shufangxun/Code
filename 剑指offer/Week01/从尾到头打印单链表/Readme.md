**题目**  
输入一个链表的头结点，按照 从尾到头 的顺序返回节点的值。
返回的结果用数组存储。

**算法**  
从头到尾遍历链表，用栈存储每个节点的值，用insert()模拟栈，一直在index=0的位置插入遍历的值。


