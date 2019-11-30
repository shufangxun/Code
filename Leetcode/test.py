def lengthOfLongestSubstring(s):
        lookup = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in lookup:
                i = max(lookup[s[j]], i)
            ans = max(ans, j - i + 1)
            lookup[s[j]] = j + 1
        return ans
s = list([1,2,4,2])
a = lengthOfLongestSubstring(s)
print(a)