def findT2(array,T):
    

    '''
    二分法
    运行时间：440ms
    占用内存：5840k
        '''
    rows = len(array)
    columns = len(array[0])
    for i in range(rows):
        low = 0
        high = columns - 1
        while low < high:
            mid = (low + high) // 2   ## 向下取整
            if T > array[i][mid]:
                low = mid + 1
            elif T < array[i][mid]:
                high = mid - 1
            else:
                return True
    return False

if __name__ == "__main__":
    arr = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print(findT2(arr,7))
