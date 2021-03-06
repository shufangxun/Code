**题目** 

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。

如果是则返回true，否则返回false。

假设输入的数组的任意两个数字都互不相同。

**样例** 
```
输入：[4, 8, 6, 12, 16, 14, 10]

输出：true
```


**算法**


- 二叉搜索树的性质  
  左子树上所有节点的值均小于它的根节点；右子树上所有节点的值均大于它的根节点。
- 二叉搜索树后序遍历的性质  
  序列最后一个数字是根节点，序列剩余部分分成两部分，前一部分是左子树，后一部分是右子树。

**递归法**  

对于二叉搜索树的后序遍历的序列来说，最后一个元素即是它的根节点，序列的前某部分元素全部小于最后一个元素，序列的后某部分元素全大于最后一个元素。

先判断数组的左子树和右子树的位置，然后再判断左子树、右子树是不是二叉搜索树

**循环法**  
对于一个二叉搜索树来说，根节点的左子树每个节点的值肯定小于右子树每个节点的值，所以可以不断的去去掉序列的最后一个值，并且把剩下的部分分成小于最后一个值和大于最后一个值的两部分，只要能分出来那就说明符合二叉搜索树的定义，否则就不符合。