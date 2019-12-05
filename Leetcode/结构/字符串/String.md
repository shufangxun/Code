# 字符串

## 字符串操作

### 反转字符串

> 将输入的字符串反转过来，并且是$O(1)$空间解决这一问题。

解法1：双指针法

```python
def reverseString(s):
    if len(s) <= 1:
        return s
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s
```

解法2：三次异或法

```python
'''
交换a,b:
a = a ^ b
b = b ^ a
a = a ^ b
'''
def reverseString(s):
    if len(s) <= 1:
        return s
    l, r = 0, len(s) - 1
    while l < r:
        s[l] ^= s[r]
        s[r] ^= s[l]
        s[l] ^= s[r]
        l += 1
        r -= 1
    return s
```

### 反转字符串 I I

> 给定一个字符串和一个整数 k，从字符串开头算起的每个 2k 个字符的前 k 个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。

解法：反转k个 跳过k个 最后剩余的不够k个,全部反转

```python
def reverseStr(s, k):
    left, mid, right = 0, k, 2 * k                  # 初始化左中右指针
    res = ''                                        # 初始化结果字符串
    while len(res) < len(s):                        # 满足条件时执行
        res += s[left:mid][::-1] + s[mid:right]     # 把当前单元的结果添加到结果字符串
        left, mid, right = left + 2 * k, mid + 2 * k, right + 2 * k
    return res
```

### 旋转字符串

> 给定一个字符串和一个偏移量，根据偏移量原地移动字符串，空间复杂度 $O(1)$
> 输入: str="abcdefg", offset =2
> 输出: str = "cdefgab"

- 空间复杂度：$O(1)$
- 时间复杂度：$O(n)$

```python
def rotateString(s, offset):
    if not s:
        return s
    offset = offset % len(s) # 细节
    reverse(s, 0, offset - 1)
    reverse(s, offset, len(s) - 1)
    reverse(s, 0, len(s) - 1)
    return s
def reverse(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
```

## 字符串性质

### 最后一个单词长度

> 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。如果不存在最后一个单词，请返回 0 。

- 去掉空格再计数
- 时间复杂度：$O(n)$

```python
def lengthOfLastWord(self, s):
    # num是长度
    num = 0
    end = len(s) - 1
    # 去掉空格
    while end >= 0 and s[end] == ' ':
        end -= 1
    # 再计数
    while end >= 0 and s[end] != ' ':
        num += 1
        end -= 1
    return num
```

### 无重复的最长子串

见动态规划和滑动窗口

### 最小覆盖子串

见滑动窗口

### 至多包含两个不同字符串的最长子串

见滑动窗口

### 最长回文子串

见动态规划

### 判断子序列

> 给定字符串 s 和 t ，判断 s 是否为 t 的子序列

```bash
s = "abc", t = "ahbgdc"
return true
```

三种解法：1. 双指针 2. 动态规划 3. 贪心算法

## 字符串匹配

### 有效括号

> 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效

思路：栈匹配
解题思路：

- 建立哈希表 dic 构建左右括号对应关系：key 左括号，value 右括号
- 建立栈 stack，遍历字符串 s 并按照算法流程一一判断
  - 若遇到左括号，入栈，遇到右括号时将对应栈顶左括号出栈
  - 当为合法匹配时，**遍历完所有括号后** stack 仍然为空

算法流程

- 如果 c 是左括号，则入栈 ；否则通过哈希表判断括号对应关系，若 栈顶出栈括号与当前遍历括号 c 不对应，则提前返回 false

提前返回 false

- **没有遍历完**栈就已经为空  “()][]{}”

复杂度分析

- 时间复杂度 **O(N)**：正确的括号组合需要遍历 1 遍 s；
- 空间复杂度 **O(N)**：哈希表和栈使用线性的空间大小。

```python
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        for c in s:
            if c == '(' :
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif len(stack) == 0 or c != stack.pop():
                return False
        return len(stack) == 0
```
