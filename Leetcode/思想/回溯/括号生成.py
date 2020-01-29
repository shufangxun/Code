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