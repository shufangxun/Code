class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return s
        # 用空格分割字符串, 每个字符作为一个元素
        # "shu fang xun" ==> ['shu', 'fang', 'xun']
        t = s.split(' ')

        # 翻转
        return " ".join(t[::-1])