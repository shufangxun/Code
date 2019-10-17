class Solution:
    def longestSubstringWithoutDuplication(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 动态规划法
        if len(s) == 0:
            return 0

        d = {}
        d[s[0]] = 0
        dp = [1] * len(s)
        # 求当前子串的长度
        for i in range(1, len(s)):
            if s[i] not in d.keys() or i - d[s[i]] > dp[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = i - d[s[i]]
            d[s[i]] = i # 更新字符位置
        return max(dp)  # 数组
