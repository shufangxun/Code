class Solution:
    def longestSubstringWithoutDuplication(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        d = {}
        dp = [1]*len(s)

        for i in range(1, len(s)):
            if s[i] not in d:
                dp[i] = dp[i-1] + 1
            else:
                if i - d[s[i]] > dp[i-1]:
                    dp[i] = dp[i-1] + 1
                else:
                    dp[i] = i - d[s[i]]
            d[s[i]] = i
        return max(dp)
