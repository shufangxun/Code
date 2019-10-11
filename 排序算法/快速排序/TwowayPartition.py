def quicksort(array):
    '''
        避免手动输入长度信息 http://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html
        '''
    Quicksort2(array,0,len(array)-1)
    return array

def Quicksort2(array, front, rear):

    if front < rear:
        idx = Partition(array, front, rear)
        Quicksort2(array, front, idx - 1)
        Quicksort2(array, idx + 1, rear)
    

def Partition(array, front, rear):
    '''
        双指针法：前后一起寻找
        '''
    pivot = array[front]
    while front < rear:
        while front < rear and array[rear] >= pivot: # 为什么这里重复front < rear 防止一样的重复操作
            rear -= 1
        while front < rear and array[front] < pivot:
            front += 1
        array[rear], array[front] = array[front], array[rear] ## 找到位置，直接交换 非常pythonic
    
    array[front] = pivot
    return front

if __name__ == "__main__":
    a = [1,2,4,5,6,2,3,2]
    print(quicksort(a))


