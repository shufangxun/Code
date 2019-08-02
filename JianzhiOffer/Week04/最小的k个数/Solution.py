class Solution(object):
    def getLeastNumbers_Solution(self, input, k):
        """
        :type input: list[int]
        :type k: int
        :rtype: list[int]
        """
        n = len(input)
        if k <= 0 or k > n:
            return []
        start = 0
        end = n - 1
        mid = self.partition(input, start, end)
        while k - 1 != mid:
            if k - 1 > mid:
                start = mid + 1
                mid = self.partition(input, start, end)
            elif k - 1 < mid:
                end = mid - 1
                mid = self.partition(input, start, end)
        res = input[:mid+1]
        res.sort()
        return res
        
    


    def partition(self, input, start, end):
        pviot = input[start]
        while start < end:
            while start < end and pviot >= input[start]:
                start += 1
            while start < end and pviot <= input[end]:
                end -= 1
            input[start], input[end] = input[end], input[start]
        
        input[start] = pviot
        return start  # start 已经变化
        