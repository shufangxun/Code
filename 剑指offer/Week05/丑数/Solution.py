class Solution(object):
    def getUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = j = k = 0
        res = [0] * n # 开辟空间,不能res = []
        res[0] = 1
        for s in range(1,n):
            res[s] = min(res[i] * 2, min(res[j] * 3, res[k] * 5))
            if res[s] == res[i] * 2:
                i += 1
            if res[s] == res[j] * 3: # 不用else是为了去重: 6 = 2 * 3
                j += 1
            if res[s] == res[k] * 5:
                k += 1
        return res.pop()
