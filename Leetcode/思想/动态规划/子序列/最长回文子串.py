# 法1
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        # 初始化为False
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        maxlen, res = 1, s[0]
        for right in range(1, len(s)):
            for left in range(right):
                # 包含长度为1和2的情况 关键所在
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
                    curlen = right - left + 1
                    if curlen > maxlen:
                        maxlen = curlen
                        res = s[left : right + 1]
        return res

# 法2
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        maxlen, res = 1, s[0]
        for i in range(len(s)):
            odd, lenodd = self.spreadCenter(s, i, i)
            even, leneven = self.spreadCenter(s, i, i + 1)
            curS = odd if lenodd >= leneven else even
            if len(curS) > maxlen:
                maxlen = len(curS)
                res = curS
        return res
    # 提前计算了长度和序列
    def spreadCenter(self, s, i, j):
        left, right = i, j
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right], right - left - 1

# 法2变形
class Solution3:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        left, right = 0, 0
        for i in range(len(s)):
            lenodd = self.spreadCenter(s, i, i)
            leneven = self.spreadCenter(s, i, i + 1)
            length = max(lenodd, leneven)
            # 重新分配左右边界
            if length > right - left:
                left = i - (length - 1) // 2
                right = i + length // 2
        return s[left: right + 1]
    # 只根据长度操作
    def spreadCenter(self, s, i, j):
        left, right = i, j
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

# 法4 马拉车