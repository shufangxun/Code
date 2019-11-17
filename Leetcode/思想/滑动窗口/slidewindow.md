# 滑动窗口

## 滑动窗口的最大值(元素) [参考](https://blog.csdn.net/u010429424/article/details/73692248)  

>1．给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。  
>2．返回滑动窗口中的最大值(元素)

```python
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
```

借助一个双端队列，从头遍历数组，根据如下规则进行入队列或出队列操作：

1. 如果队列为空，则当前数字入队列
2. 如果当前数字大于队列尾，则删除队列尾，直到当前数字小于等于队列尾，或者队列空，然后当前数字入队列
3. 如果当前数字小于队列尾，则当前数字入队列
4. 如果队列头超出滑动窗口范围，则删除队列头
5. 这样能始终保证队列头为当前的最大值
6. 队列中存储数组的下标而非数值，这样通过判断下标之间的差值是否大于窗口的大小

```python
def maxSlidingWindow(self, nums, k):
    if len(nums) < k:
        return []
    window, res = [], []
    for i, num in enumerate(nums):
        if i >= k and window[0] <= i - k:
            window.pop(0)
        while window and num >= nums[window[-1]]:
            window.pop(-1)
        window.append(i)
        if i >= k - 1:
            res.append(nums[window[0]])
    return res
```

## 无重复的最长子串

> 给定一个字符串，请你找出其中不含有重复字符的最长子串的长度

- 滑动窗口法
- 模拟一个滑动窗口，窗口内是无重复的字符，要尽可能的扩展窗口长度
  - 用一个left变量来指向滑动窗口的左边界，如果遍历到的字符没有出现过，扩大右边界
  - 如果出现过，分两种情况讨论：
    - 当前字符出现在滑动窗口内，把已在滑动窗口内的字符去掉，然后加进来，去掉的方法是通过移动left指针，因为之前的哈希表保存了该字符最后出现的位置，所以只要移动left指针
    - 当前字符没有在滑动窗口内，可以直接加到滑动窗口内。
  - 只维护一个res结果，每次用出现的窗口大小和res本身比较，就可以得到最终结果。

```python
def lengthOfLongestSubstring(s):
    left = -1
    ans = 0
    # 字符转ASCII ord(s)
    lookup = [-1] * 128
    for i, item in range(s):
        # 出现在滑动窗口内
        if lookup[ord(s[i])] > left:
            left = lookup[ord(s[i])]
        # 当前字符是无重复的 or 未出现在滑动窗口内
        ans = max(ans, i - left)
        lookup[ord(s[i])] = i
```

## 最小覆盖子串

> Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

示例

```python
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
```

思路；滑动窗口＋哈希表

1. 初始化左右指针$(lef=right=0)$，闭区间$[left, right]$是窗口范围
2. 移动右指针，直到窗口内字符串包含 T 的所有字符
3. 移动左指针，找到符合条件的最小窗口，更新最小窗口长度
   1. 当不包含所有字符串时，重复２操作
4. 重复上面两步直到右指针到终点

总结；移动右指针找到可行解，移动左指针找到最优解

重点：用**哈希表**作计数器判断窗口包含所有T的所有字符

- 哈希表 valid 记录 T 中包含的字符及出现次数
- counter 统计 T 的长度
  - 当 counter == 0 时，说明窗口包含了所有 T 字符

时间复杂度：$O(len(s) + len(t))$  
空间复杂度：$O(len(t)$

```python
def minWindow(self, s: str, t: str) -> str:
    valid = [0] * 128
    counter = len(t) # 子串是否符合条件
    left, right = 0, 0
    minlen = len(s) # 最小长度最坏情况下是 len(s)
    res = "" # 子串
    # 初始化 valid
    for i in range(len(t)):
        valid[ord(t[i])] += 1
    # 找到可行解
    while right < len(s):
        # 当包含 t 字符时 counter - 1
        if valid[ord(s[right])] > 0:
            counter -= 1
        # 包含的减1，不包含的变为负
        valid[ord(s[right])] -= 1
        # 当窗口包含所有 T 字符
        while counter == 0:
            # 恢复计数，因为之前做了减1操作
            valid[ord(s[left])] += 1
            # 当移动左指针会让窗口不符合条件时
            if valid[ord(s[left])] > 0:
                counter += 1
                if right - left + 1 <= minlen:
                    minlen, res = right - left + 1, s[left:right+1]
            left += 1
        # 不管是否找到，都移动右指针
        right += 1
    return res
```
