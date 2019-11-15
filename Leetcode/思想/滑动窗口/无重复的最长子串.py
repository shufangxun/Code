class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = -1
        ans = 0
        lookup = [-1] * 128
        for i, item in enumerate(s):
            if lookup[ord(s[i])] > left:
                left = lookup[ord(s[i])]
            ans = max(ans, i - left)
            lookup[ord(s[i])] = i
        return ans