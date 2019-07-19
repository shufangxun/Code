class Solution:
    def verifySequenceOfBST(self, sequence):
        """
        :type sequence: List[int]
        :rtype: bool
        """
        # python 风格
        # 递归中止条件
        if not sequence:
            return True

        # 根节点
        root_val = sequence.pop()
        left_end = -1
         
        # 用 enumerate 
        for i, num in enumerate(sequence):
            if num > root_val:
                break
            left_end = i
        for num in sequence[left_end+1:]:
            if num < root_val:
                return False

        # 递归
        ans = True
        ans = ans and self.verifySequenceOfBST(sequence[:left_end+1])  if left_end >= 0 else ans
        ans = ans and self.verifySequenceOfBST(sequence[left_end+1:])  if left_end+1 < len(sequence) else ans
        return ans


        