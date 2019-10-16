class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # 前序遍历
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        res = ''
        if root is None:
            return '! '
        res += str(root.val)
        res += ' '
        res += self.serialize(root.left)
        res += self.serialize(root.right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(' ')
        return self.__helper(arr)

    def __helper(self, arr):
        while arr:
            top = arr.pop(0)
            if top != '!':
                root = TreeNode(int(top))
                root.left = self.__helper(arr)
                root.right = self.__helper(arr)
                return root
            else:
                return None
