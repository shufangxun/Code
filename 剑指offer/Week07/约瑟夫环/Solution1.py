class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        alive = n # 幸存总人数
        state = [1] * n # 每个人的状态
        count = 0 # 计数
        index = 0 # 循环用
        while alive:
            count += state[index]
            if count == m:
                alive -= 1
                state[index] = 0
                count = 0
            
            index = (index + 1) / count # 在count之间循环

        return index