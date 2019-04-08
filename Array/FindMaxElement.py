def FindMax(array,T):
    ## 获得数组的行和列
    ### 运行时间：228ms
    ### 占用内存：5624k
    rows = len(array)
    columns = len(array[0])

    ## 初始化--右上角 i:行 j:列
    i = 0  
    j = columns - 1

    while i < rows and j >= 0:
        if T == array[i][j]:
            return True        
        elif T < array[i][j]:
            j -= 1
        else:
            i += 1

    ## 循环里没有则返回False        
    return False
'''
def FindMax(array,T):
    ### 每一行做二分法
    ### 运行时间：440ms
    ### 占用内存：5840k
    rows = len(array)
    columns = len(array[0])
    for i in range(rows):
        low = 0
        high = columns - 1
        while low < high:
            mid = (low + high)/2
            if T > array[i][mid]:
                low = mid + 1
            elif T < array[i][mid]:
                high = mid - 1
            else:
                return True

    return False
'''
    
if __name__ == "__main__":
    arr = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print(FindMax(arr,7))
