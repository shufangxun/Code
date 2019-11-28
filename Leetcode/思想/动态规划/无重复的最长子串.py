def LSWB(s):
    if len(s) <= 1:
        return len(s)
    else:
        idx = dict()
        idx[s[0]] = 0
        dp = [1] * len(s)
        for i in range(1, len(s)):
            if s[i] not in idx.keys() or i - idx[s[i]] > dp[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = i - idx[s[i]]
            idx[s[i]] = i
    return max(dp)