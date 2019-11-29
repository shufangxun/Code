# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    # 先中序遍历存到数组,然后双指针
    def findTarget(self, root, k):
        nums = []
        self.inorder(root, nums)
        l, r = 0, len(nums) - 1
        while l < r:
            curSum = nums[l] + nums[r]
            if curSum == k:
                return True
            elif curSum < k:
                l += 1
            else:
                r -= 1
        return False

    def inorder(self, root, nums):
        if root is None: return
        self.inorder(root.left, nums)
        nums.append(root.val)
        self.inorder(root.right, nums)

    # 边遍历边查找，遍历的时候存入哈希表中
    def findTarget(self, root, k):
        if not root: return False
        bfs, s = [root], set()
        for node in bfs:
            if k - node.val in s: return True
            s.add(node.val)
            if node.left: bfs.append(node.left)
            if node.right: bfs.append(node.right)
        return False
