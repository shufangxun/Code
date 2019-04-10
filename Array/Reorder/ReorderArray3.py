def reorderArray3(array):
    '''
    solution 3
    列表 list 
    insert(i,v) 在index i之前插入v
    运行时间：23ms
    占用内存：5856k
        '''
    newIndex = -1
    for i in range(len(array)):
        if array[i] % 2:  ## 当为奇数
            newIndex += 1
            array.insert(newIndex, array.pop(i))  
    return array 


if __name__ == "__main__":
     arr = [1,2,3,4,5]
     print(reorderArray3(arr))  