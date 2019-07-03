class Solution(object):
    def numberOf1Between1AndN_Solution(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        count = 0
        base, round = 1, n
        while round :
            weight = round % 10
            round = round // 10   # 当前位的前面位
            count += base * round
            if  weight > 1:
                count += base
            if weight == 1:
                count += (n % base) + 1
            base *= 10

        return count