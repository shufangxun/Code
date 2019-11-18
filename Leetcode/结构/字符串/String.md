# 字符串

## 反转字符串

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

## 旋转字符串

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

## 最后一个单词长度

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

## 无重复的最长子串

见动态规划和滑动窗口

## 最小覆盖子串

见滑动窗口

## 至多包含两个不同字符串的最长子串

见滑动窗口

## 最长回文子串

见动态规划

