def MinInRotate(array):
    low = 0
    high = len(array) - 1
    '''
        分三类：
        1.特殊情况：值为0和1
        2.旋转值为0，即为原数组
        3.中间、头和尾值一样
        4.正常操作

        运行时间：661ms
        占用内存：5712k
        '''
    if low == high:
        return array[low]
    elif high == -1:
        return 0 
    elif array[low] < array[high]:
        return array[low]
    else:
        ## 当两者间距为1时，跳出循环,最小值存储于array[high]
        while (high - low) > 1:
            mid = (low + high) // 2
            if array[mid] >= array[low]: ## 在前一个序列中
                low = mid
            elif array[mid] <= array[high]: ## 在后一个序列中
                high = mid
            elif array[mid] == array[high] == array[low]: ## 特殊情况:[1,1,1,0,1,1]
                for i in range(1,len(array)):
                    if array[i] < array[low]:
                        high = i  ## 为了统一输出
        return array[high]

if __name__ == "__main__":
    arr = [1,1,1,0,1,1]
    s = MinInRotate(arr)
    print(s)
        

            



