**题目**  

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

**样例**  
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

**算法**
- hashmap   
  时间复杂度:  
  第一层for循环是O(n)，字典采用的是hash函数的结构，所以在 x in dict的查找过程中，时间复杂度为O(1)，这里没用到index查询，直接获取value值，字典的Get Item的复杂度也是O(1)，所以整个算法的时间复杂度为O(n)　　
  
  空间复杂度:  
  O(n)，用空间换时间