**题目**  

输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。

例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以结果打印出3个连续序列1～5、4～6和7～8。

**样例**  
```
输入：15

输出：[[1,2,3,4,5],[4,5,6],[7,8]]
```

**算法**  
双指针法，不同之处在于判断多个元素和
