def morethanHalf(array):
    ## 统计数组中出现次数过半的元素
    '''
        数组法:初始化res为a[0]和标识为1
               当下一个元素相同时，标识+1，否则-1
               当标识为0时，重置为1，res变为a[i]
               最后一次重置的元素就保存在res中，统计次数
        运行时间: 25ms  
        占用内存: 5756k
        复杂度: O(n)
        '''
    L = len(array)
    res = array[0]
    label = 1
    for i in range(1,L):
        if label == 0:
            label += 1
            res = array[i]
        elif array[i] == res:
            label += 1
        else:
            label -= 1

    count = 0
    for i in range(L):
        if array[i] == res:
            count += 1
    
    return res if count*2 > L else 0

if __name__ == "__main__":
    arr = [1,2,2,2,2,3,4]
    print(morethanHalf(arr))
