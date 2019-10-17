class Solution(object):
    def findNumberAppearingOnce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        for num in dict:
            if dict[num] == 1:
                return num
                

         