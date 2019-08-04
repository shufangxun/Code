import heapq
class Solution(object):
    def getLeastNumbers_Solution(self, input, k):
        """
        :type input: list[int]
        :type k: int
        :rtype: list[int]
        """
        data = []
        for elem in input:
            elem = -elem
            # [-1,-5,-8] 最小的是-8
            if len(data) < k:
                heapq.heappush(data, elem)
            else:
                least = data[0]
                if elem > least: # -2 > -8
                    heapq.heapreplace(data, elem)

        return sorted([-x for x in data])