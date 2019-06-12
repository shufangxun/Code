class Solution(object):
    def replaceSpaces(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not isinstance(s, str) or len(s) < 0 or s == None:
            return ' '

        ## step1
        space = 0
        for i in s:
            if i == ' ':
                space += 1 
        
        s_new = s + 2 * space * ' ' # 扩充原数组,减少空间开销
        s_new = list(s_new)  # 字符数组才能更改

        ## step2
        i = len(s) - 1
        j = len(s_new) - 1

        while i >= 0:
            if s_new[i] == ' ':
                s_new[j - 2 : j + 1] = ['%', '2', '0']
                j -= 3
                i -= 1
            else:
                s_new[j] = s_new[i]
                j -= 1
                i -= 1
        
        return ''.join(s_new)  # 再变回字符
            
        
