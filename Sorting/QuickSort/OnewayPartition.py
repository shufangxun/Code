def quicksort(array):
    '''
    https://www.jianshu.com/p/daebe1596ca6
        '''
    Quicksort2(array,0,len(array)-1)
    return array

def Quicksort2(array, front, rear):

    if front < rear:
        idx = partition(array, front, rear)
        Quicksort2(array, front, idx - 1)
        Quicksort2(array, idx + 1, rear)


def partition(array, front, rear):
        pivot = array[front]
        for i in range(front + 1, rear + 1):
            if array[i] <= pivot:
                front += 1
                array[i], array[front] = array[front], array[i]
        array[pivot], array[front] = array[front], array[pivot]
        return pivot

