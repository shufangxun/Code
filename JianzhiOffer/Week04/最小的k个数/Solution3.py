class Solution(object):
    def getLeastNumbers_Solution(self, input, k):
        """
        :type input: list[int]
        :type k: int
        :rtype: list[int]
        """
        if k <= 0 or k > len(input):
            return []
        # 建立最大堆
        for i in range(int(k / 2) - 1, -1, -1):
            self.heapAjust(input, i, k - 1)

        for i in range(k, len(input)):
            if input[i] < input[0]:
                input[0], input[i] = input[i], input[0]
                # 调整前k个数
                self.heapAjust(input, 0, k - 1)
                
        return sorted(input[:k])
 
    def heapAjust(self, nums, start, end):
        temp = nums[start]
        # 记录较大的那个孩子下标
        child = 2 * start + 1
        while child <= end:
            # 比较左右孩子，记录较大的那个
            if child + 1 <= end and nums[child] < nums[child + 1]:
                # 如果右孩子比较大，下标往右移
                child += 1
            # 如果根已经比左右孩子都大了，直接退出
            if temp >= nums[child]:
                break
            # 如果根小于某个孩子,将较大值提到根位置
            nums[start] = nums[child]
            # nums[start], nums[child] = nums[child], nums[start]
            # 接着比较被降下去是否符合要求，此时的根下标为原来被换上去的那个孩子下标
            start = child
            # 孩子下标也要下降一层
            child = child * 2 + 1
        # 最后将一开始的根值放入合适的位置(如果前面是交换，这句就不要)
        nums[start] = temp