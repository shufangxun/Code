class Solution:
    def longestPalindrome(self, s):
        ans = 0
        from collections import defaultdict
        # 构建哈希表
        counter = defaultdict(int)
        
        for c in s:
            counter[c] += 1

        for v in counter.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans

class Solution:
    def longestPalindrome(self, s):
        from collections import defaultdict
        # 构建哈希表
        counter = defaultdict(int)
        
        for c in s:
            counter[c] += 1

        count = 0 
        for v in counter.values():
            count += v % 2
        
        if count == 0:
            return len(s)
        else:
            return len(s) - count + 1