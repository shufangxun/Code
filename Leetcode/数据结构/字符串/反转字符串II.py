class Solution1:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            if i + k >= len(s):
                self.reverse(s, i, len(s) - 1)
            else:
                self.reverse(s, i, i + k - 1)
        return ''.join(s)

    def reverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

class Solution2:
    def reverseStr(self, s: str, k: int) -> str:
        left, mid, right = 0, k, 2 * k                  # 初始化左中右指针
        res = ''                                        # 初始化结果字符串
        while len(res) < len(s):                        # 满足条件时执行
            res += s[left:mid][::-1] + s[mid:right]     # 把当前单元的结果添加到结果字符串
            left, mid, right = left + 2 * k, mid + 2 * k, right + 2 * k                          
        return res   