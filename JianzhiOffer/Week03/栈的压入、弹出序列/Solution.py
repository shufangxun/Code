class Solution(object):
    def isPopOrder(self, pushV, popV):
        """
        :type pushV: list[int]
        :type popV: list[int]
        :rtype: bool
        """
    
        if len(pushV) != len(popV):
            return False
        if not pushV and not popV:
            return True
        
        stack = []
        for v in pushV:
            stack.append(v)
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        return True if not stack else False
