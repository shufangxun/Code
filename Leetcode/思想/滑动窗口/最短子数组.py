class Solution:
    def getLength(self, arr):
        minlen = -1
        lookup = {}
        for i in range(len(arr)):
            if arr[i] in lookup:
                curlen = i - lookup[arr[i]] + 1
                if minlen == -1:
                    minlen = curlen
                else:
                    minlen = min(minlen, curlen)
            lookup[arr[i]] = i
        return minlen