# 法1
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, ans = -1, 0
        lookup = [-1] * 128
        for i in range(len(s)):
            # 前一个出现在窗口内
            if lookup[ord(s[i])] > left:
                left = lookup[ord(s[i])]
            ans = max(ans, i - left)
            lookup[ord(s[i])] = i
        return ans

# 法2
def lengthOfLongestSubstring(s):
    lookup = {}
    i, ans = 0, 0
    for j in range(len(s)):
        if s[j] in lookup:
            i = max(lookup[s[j]], i)
        ans = max(ans, j - i + 1)
        lookup[s[j]] = j + 1
    return ans

# 法3
def lengthOfLongestSubstring(s):
    lookup = [0] * 128
    left, right = 0, 0
    counter = 0
    maxlen = 0
    while right < len(s):
        # 当右指针元素之前出现过，计数加１
        if lookup[ord(s[right])] > 0:
            counter += 1
        # 不管出没出现，都需要统计出现次数，移动右指针
        lookup[ord(s[right])] += 1
        right += 1
        while counter > 0:
            # 当有重复时
            if lookup[ord(s[left])] > 1:
                counter -= 1
            # 这一步操作不懂
            lookup[ord(s[left])] -= 1
            left += 1
        maxlen = max(maxlen, right - left)
    return maxlen

