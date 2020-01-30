class Solution:
    def numDecodings1(self, s: str) -> int:
        n = len(s)
        if(not s or s[0] == '0'):
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1,n):
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    dp[i + 1] = dp[i - 1]
                else:
                    return 0
            else:
                if s[i - 1] == "1" or (s[i - 1] == "2" and "1" <= s[i] <= "6"):
                    dp[i + 1] = dp[i] + dp[i - 1]
                else:
                    dp[i + 1] = dp[i]
        return dp[-1]

    def numDecodings2(self, s: str) -> int:
        if(not s or s[0] == '0'):
            return 0
        n = len(s)
        pre, cur = 1, 1
        for i in range(1, n):
            tmp = cur
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    cur = pre
                else:
                    return 0
            else:
                # 这一步隐含了 dp[i+1] = dp[i]
                # 即加一个数数目不变 所以直接输出cur就行
                if s[i - 1] == "1" or (s[i - 1] == "2" and "1" <= s[i] <= "6"):
                    cur = cur + pre
            pre = tmp
        return cur


