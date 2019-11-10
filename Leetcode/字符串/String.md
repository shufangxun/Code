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

## 循环移动字符串

> 给定一个字符串和一个偏移量，根据偏移量原地移动字符串，空间复杂度 $O(1)$  
> 输入: str="abcdefg", offset =2  
> 输出: str = "cdefgab"  

- 空间复杂度：$O(1)$
- 时间复杂度：$O(n)$

```python
def rotateString(s, offset):
    if not s:
        return s
    offset = offset % len(s)
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
