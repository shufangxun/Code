class Solution:
    def firstNotRepeatingChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = dict()
        for i in range(len(s)):
            if s[i] not in d.keys():
                d[s[i]] = 1
            else:
                d[s[i]] += 1

        for i in range(len(s)):
            if d[s[i]] == 1:
                return s[i]

        return '#'