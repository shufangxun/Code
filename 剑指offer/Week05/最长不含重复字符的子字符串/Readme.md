**题目**  

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

假设字符串中只包含从’a’到’z’的字符。

**样例**  
```
输入："abcabc"

输出：3
```

**算法**

- 滑动窗口法
    - 设置一个**按照输入顺序**存储的集合, 当发现当前元素时, 按照顺序删除直到当前元素  
    [参考](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/python-hua-dong-chuang-kou-xun-xu-jian-jin-de-3ge-/)

- 动态规划法  
  用f(i)表示以i个字符结尾不包含重复子字符串的最长长度，从左向右扫描

1. 若第i个字符在之前没出现过或出现了但是出现在当前子串前面，那么 f(i) = f(i-1) + 1;

2. 若第i个字符在之前出现过，且出现在当前子串中间,则是两个重复子串之间 f(i) = i - dict[s[i]]

   