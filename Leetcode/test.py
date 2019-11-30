def lengthOfLongestSubstring(s):
        lookup = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in lookup:
                i = max(lookup[s[j]], i)
            ans = max(ans, j - i + 1)
            lookup[s[j]] = j + 1
        return ans

def test(s):
    left, ans = -1, 0
    lookup = {}
    for i in range(len(s)):
        if s[i] in lookup:
        # 前一个出现在窗口内
            if lookup[s[i]] > left:
                left = lookup[s[i]]
        ans = max(ans, i - left)
        lookup[s[i]] = i
    return ans
s = list([1,2,4,2])
a = test(s)
print(a)