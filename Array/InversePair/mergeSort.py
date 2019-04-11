'''
    递归版：
    sort 和 merge 结合
    '''

def mergeSort(array):
    '''
        将数组划分成小份，进行归并操作 
        '''
    if len(array) <= 1:
        return array
    
    ## 划分数组
    mid = len(array) // 2
    leftPart = array[:mid]
    rightPart = array[mid:]

    ## 对划分的数组排序
    leftPart = mergeSort(leftPart)
    rightPart = mergeSort(rightPart)

    return merge(leftPart, rightPart)

def merge(leftPart, rightPart):
    '''
        归并的实现
        '''
    res = []
    while leftPart and rightPart:     ## 这个条件控制其中一个全部归并： 4578 1236
        if leftPart[0] < rightPart[0]:
            res.append(leftPart.pop(0))   ## pop(0)的好处始终指向第一个元素，自动实现指向下一个元素
        else:
            res.append(rightPart.pop(0))
    
    if leftPart:
        res += leftPart
    else:
        res += rightPart
    
    return res


if __name__ == "__main__":
    arr = [9,8,7,6,5,4,3,2,1]
    print(mergeSort(arr))
    

