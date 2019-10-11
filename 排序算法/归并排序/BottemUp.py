'''
思路:
    循序渐进，先将所有2元素数组sort,然后所有两两归并得四,所有四四归并得八....

'''

class mergeSort:

    def __init__(self, length = 4):
        self.length = length

    def merge(self, aLeft, aRight):
        i, j = 0, 0
        sortedArray = []  ## 辅助函数
        # 优化2.直接复制，不归并
        if aLeft[-1] <= aRight[0]:    ## 问题出在这里
            sortedArray = aLeft + aRight
            return sortedArray
        
        while i < len(aLeft) and j < len(aRight):
            if  aLeft[i] < aRight[j]:
                sortedArray.append(aLeft[i])
                i += 1
            else:
                sortedArray.append(aRight[j])
                j += 1
        # 当某一个遍历结束时，直接复制剩余
        sortedArray += aLeft[i:]
        sortedArray += aRight[j:]

        return sortedArray
    
    def sort(self, alist):
        sz = 1 # 子数组尺寸
        a = []
        while sz < len(alist):
            for i in range(0, len(alist), 2 * sz):
               a += merge(alist[i:i+sz], alist[i+sz,i+2*sz])

            sz = sz * 2



