class Solution:
    def firstNotRepeatingChar(self, s):
        """
        :type s: str
        :rtype: str
        """

        for i in range(0,len(s)):
            if s[i] not in s[:i]+s[i+1:]: # 精髓
                return s[i]
        return "#"