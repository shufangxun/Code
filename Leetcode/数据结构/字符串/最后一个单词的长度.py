class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # num是长度
        num = 0
        end = len(s) - 1
        # 去掉空格
        while end >= 0 and s[end] == ' ':
            end -= 1
        # 再计数
        while end >= 0 and s[end] != ' ':
            num += 1
            end -= 1
        return num