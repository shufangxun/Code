class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        r, pviot = 0, x
        while pviot:
            r = pviot % 10 + r * 10
            pviot = pviot // 10
        if r == x:
            return True
        return False

