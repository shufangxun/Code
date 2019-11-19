# 法1
class Solution:
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




