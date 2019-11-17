class Solution(object):
    def minWindow(self, s: str, t: str) -> str:
        valid = [0] * 128
        counter = len(t) # 子串是否符合条件
        left, right = 0, 0
        minlen = len(s) # 最小长度最坏情况下是 len(s)
        res = "" # 子串
        # 初始化 valid
        for i in range(len(t)):
            valid[ord(t[i])] += 1
        # 找到可行解
        while right < len(s):
            # 只有包含子串时才操作
            if valid[ord(s[right])] > 0:
                counter -= 1
            # 包含的减1，不包含的变为负
            valid[ord(s[right])] -= 1
            # 不管是否找到，都移动右指针
            right += 1
            # 当所有子串都包含
            while counter == 0:
                # 恢复计数，因为之前做了减1操作
                valid[ord(s[left])] += 1
                # 移动左指针会使得窗口不符合条件时
                if valid[ord(s[left])] > 0:
                    counter += 1
                    if right - left + 1 <= minlen:
                        minlen, res = right - left + 1, s[left:right+1]
                left += 1
        return res