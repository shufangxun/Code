class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs("", res, n, n)
        return res

    def dfs(self, sublist, res, left, right):
        if left == 0 and right == 0:
            res.append(sublist)
        if right < left:
            return
        if left > 0:
            self.f(sublist + '(', res, left-1, right)
        if right > 0:
            self.f(sublist + ')', res, left, right-1)

# 回溯法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curlist = []
        self.dfs(curlist, res, n, n)
        return res
    def dfs(self, curlist, res, left, right):
        if left == 0 and right == 0:
            res.append(''.join(curlist))
            return 
        if right < left or left < 0 or right < 0:
            return
        
        curlist.append('(')
        self.dfs(curlist, res, left-1, right)
        curlist.pop()

        curlist.append(')')
        self.dfs(curlist, res, left, right-1)
        curlist.pop()