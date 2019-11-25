# 除了某个元素只出现一次以外，其余每个元素均出现两次
class Solution0:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res

# 除了某个元素只出现一次以外，其余每个元素均出现了三次
# 法1
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(0, 32):
            mask = 1 << i
            count = 0
            # 统计与的数目
            for j in range(len(nums)):
                if nums[j] & mask:
                    count += 1
            if count % 3:
                res = res | mask
        return self.convert(res)
    ## python 类型也是对象，所以负数没法获得
    def convert(self,x):
        if x >= 2**31:
            x -= 2**32
        return x

# 法2
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        a, b = 0, 0
        for num in nums:
            a = (a ^ num) & ~b
            b = (b ^ num) & ~a
        return a

# 恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)<2: return []
        res1, res2 = 0, 0
        r = 0
        for num in nums:
            r ^= num
        # a & (-a) 可以获得a最低的非0位
        # 比如 a 的二进制是 10000，-a 等价于取反后加1，取反就是01111，加1就是10000，最后整体相与的结果就是00000010000
        count = r & -r
        for num in nums:
            if num & count:
                res1 ^= num
            else:
                res2 ^= num
        return [res1, res2]