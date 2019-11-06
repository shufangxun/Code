class Solution(object):
    def inorderSuccessor(self, q):
        if q.right:
            q = q.right
            while q.left:
                q = q.left
            return q
        else:
            if q.father.left = q:
                return q.father
            else:
                while q.father and q.father.right == q:
                    q = q.father
                return q.father