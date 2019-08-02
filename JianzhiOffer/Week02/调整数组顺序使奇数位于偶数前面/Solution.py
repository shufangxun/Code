class Solution(object):
    def reOrderArray(self, array):
        """
        :type array: List[int]
        :rtype: void
        """
        l, r = 0, len(array) - 1
        while l < r:
            while l < r and array[l] % 2 == 1:
                l += 1
            while l < r and array[r] % 2 == 0:
                r -= 1
            if l < r:
                array[l], array[r] = array[r], array[l]
