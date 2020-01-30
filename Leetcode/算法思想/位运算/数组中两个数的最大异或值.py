class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        mask = 0
        for i in range(31, -1, -1):
            # 生成掩码
            mask |= (1 << i)
            # 当前得到的所有前缀都放在这个哈希表中
            s = set()
            # 掩码与原数依次与操作，得到前缀
            for num in nums:
                s.add(mask & num)
            # 先“贪心地”假设这个数位上是 “1” ，如果全部前缀都看完，都不符合条件，这个数位上就是 “0”
            temp = res | (1 << i)
            for prefix in s:
                if temp ^ prefix in s:
                    res = temp
                    break
        return res