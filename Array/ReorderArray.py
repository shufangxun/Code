import collections
def reorderArray(array):
    ##将数组的奇数置前，偶数置后，保持元素间的相对位置
        
    '''
    solution 1
    sorted(iterable,key,reverse=False) 默认是升序
    运行时间：24ms
    占用内存：5624k   
        '''
    return sorted(array, key=lambda x:x%2==0)

    '''
    solution 2
    双端队列 deque
    奇数从尾部查询，插入双端队列的头部，偶数从头部查询，插入双端队列的尾部，保证相对顺序
    运行时间：43ms
    占用内存：5728k
    '''
    dq = collections.deque()
    s = len(array)
    for i in range(s):
        if array[i] % 2 == 0:
            dq.append(array[i])
        if array[s-i-1] % 2 != 0:
            dq.appendleft(array[s-i-1])
    return list(dq)     

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


    
