import collections
def reorderArray2(array):
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


if __name__ == "__main__":
     arr = [1,2,3,4,5]
     print(reorderArray2(arr))  