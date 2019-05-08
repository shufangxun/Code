'''
思路：
    化整为零，将数组划分为两个子数组，一直到无法划分为止，先divide后sort + merge

函数：
    sort : divide + sort 
    merge: merge 

优化：
    1. 小数组用插入排序
    2. 当a[mid]<=a[mid+1]时，直接复制，不归并
    3. 不将元素复制到辅助数组，在每次递归调用时交换输入数组和辅助数组的角色

特点：
    归并排序适合处理大数据，时间复杂度NlogN，空间复杂度n，处理小规模数据不好，递归调用过多
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
        #当某一个遍历结束时，直接复制剩余
        sortedArray += aLeft[i:]
        sortedArray += aRight[j:]

        return sortedArray


    def sort(self, alist):
        if len(alist) == 1:
            return alist
        #优化1.当数组很小时，用插入排序
        if len(alist) <= self.length:
            return self.insertSort(alist)
        
        mid = len(alist) // 2
        aLeft = self.sort(alist[:mid])
        aRight = self.sort(alist[mid:])

        return self.merge(aLeft, aRight)
        

    
    def insertSort(self, alist):
        for i, item_i in enumerate(alist):
            index = i
            while index > 0 and alist[index - 1] > item_i:
                alist[index] = alist[index - 1]
                index -= 1
            alist[index] = item_i

        return alist

        
## 调用
if __name__ == "__main__":
    a = [1]
    print('unsorted is {}'.format(a))
    merge_sort = mergeSort()
    b = merge_sort.sort(a)
    print('sorted is {}'.format(b))


