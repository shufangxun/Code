def findelement1(array,T):
    ## 找到二维数组中的元素
    '''
    切割法
    运行时间：228ms
    占用内存：5624k
    初始化--右上角 i:行 j:列
        '''
        
    rows = len(array)
    columns = len(array[0])
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

  
if __name__ == "__main__":
    arr = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print(findelement1(arr,7))
