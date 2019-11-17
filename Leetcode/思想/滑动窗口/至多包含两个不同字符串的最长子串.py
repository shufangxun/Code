class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        lookup = [0] * 128
        left, right = 0, 0
        maxlen = 0
        counter = 0
        while right < len(s):
            # 没有出现过，即是新字符
            if lookup[ord(s[right])] == 0:
                counter += 1
            lookup[ord(s[right])] += 1
            right += 1
            # 重复字符数目大于2个
            while counter > 2:
                # 只出现一次的字符
                if lookup[ord(s[left])] == 1:
                    counter -= 1
                lookup[ord(s[left])] -= 1
                left += 1
            maxlen = max(maxlen, right - left)
        return maxlen
