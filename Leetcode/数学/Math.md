# 数学

## 回文数

> 判断一个数是否是回文数，如 121 属于回文数

法1；基本的求模得到每一位数字
法2：根据对称性，只求一边

- 判断何时处理一半
  当 x < reversed

```python
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed = 0
        while x > reversed:
            reversed = x % 10 + reversed * 10
            x = x // 10
        return x == reversed or x == reversed // 10
```

## 幂次

> 实现 pow(x, n) ，即计算 x 的 n 次幂函数

- 分治思想
- 时间复杂度：$O(logn)$
- 空间复杂度：$O(logn)$

```python
class Solution(object):
    def myPow(self, x, n):
        # 基
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        # 递归
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
```
