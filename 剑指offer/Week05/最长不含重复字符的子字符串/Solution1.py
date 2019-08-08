class Solution:
    def longestSubstringWithoutDuplication(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        maxlen = 0
        dict = {}
        for j in range(len(s)):
            if s[j] in dict and dict[s[j]] > i:
                i = dict[s[j]]
            maxlen = max(maxlen, j - i + 1)
            dict[s[j]] = j + 1
        return maxlen
