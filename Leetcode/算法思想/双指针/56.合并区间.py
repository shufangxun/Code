class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 1:
            return intervals
        u, v = 0, 0 
        # 以左端点排序
        intervals.sort(key=lambda s: s[0])
        ans = []
        while v < len(intervals):
            if intervals[u][1] < intervals[v][0]:
                # [1, 2], [3, 4]
                ans.append(intervals[u])
                u = v
            elif intervals[u][1] < intervals[v][1]:
                # [1, 3], [2, 5]
                intervals[u][1] = intervals[v][1]
                v += 1
            elif intervals[u][1] >= intervals[v][1]:
                # [1, 5], [2, 3]
                v += 1
        ans.append(intervals[u])
        return ans