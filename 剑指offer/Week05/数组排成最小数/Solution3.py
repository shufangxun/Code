class Solution(object):
    def printMinNumber(self, nums):
        # write code here
        return int("".join([str(num) for num in sorted(nums, cmp=self.cmp)]))

    def cmp(self, a, b):
        return int(str(a)+str(b)) - int(str(b)+str(a))