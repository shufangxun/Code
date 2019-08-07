class Solution:
    def longestSubstringWithoutDuplication(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = curlen = 0
        left = 0
        lookup = set()

        for i in range(len(s)):
            curlen += 1
            while s[i] in lookup:
                lookup.remove(s[i])
                left += 1
                curlen -= 1  
            if curlen > maxlen:
                maxlen = curlen
            lookup.add(s[i])

        return maxlen
        



            
        


