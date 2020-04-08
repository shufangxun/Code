class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(':')', '{':'}', '[':']'}
        stack = []
        for c in s:
            if c in dict.keys():
                stack.append(dict[c])
            elif len(stack) == 0 or c != stack.pop():
                return False
        return len(stack) == 0 