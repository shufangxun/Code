def morethanHalf2(array):
    '''
        Partition法：
        将数组排序，多于一半的必定在中位数n/2
        Partition 每次取出一个元素，与中位数比较
        '''
    L = len(array)
    low = 0
    high = L - 1
    mid = (low + high) // 2  ## 不管数目是奇偶，向下取整 
    
    ## 异常处理：当数组为空时
    if L == 0:
        return 0
        
    index = Partition(array, low, high)
    while(index != mid):
        if index > mid:
            high = index - 1
            index = Partition(array, low, high)
        else:
            low = index + 1
            index = Partition(array, low, high)
        
    res = array[index]
    count = 0
    for i in range(L):
        if array[i] == res:
            count += 1
    
    return res if count*2 > L else 0

def Partition(array, front, rear):
    pivot = array[front]
    while front < rear:
        while front < rear and array[rear] >= pivot: # 为什么这里重复front < rear
            rear -= 1
        array[front] = array[rear]
        while front < rear and array[front] < pivot:
            front += 1
        array[rear] = array[front]
    array[front] = pivot
    return front


if __name__ == "__main__":
    arr = [1,2,2,2,3,4]
    print(morethanHalf2(arr))