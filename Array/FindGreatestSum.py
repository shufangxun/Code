def findGreatestSum(array):
    ## 找到数组中和最大的子数组
    '''
        累积遍历算法 O(n)
        if i=0 or f(i-1)<=0: f(i)=array[i]
        if i!=0 and f(i-1)>0: f(i)=f(i-1)+array[i]
            
        如果当前和小于0，直接把当前和赋值为下一个元素;
        如果当前和大于0，则累加下一个元素
        运行时间：23ms
        占用内存：5728k
        '''
    if len(array) == 0:
        return False

    maxSum = array[0]
    curSum = 0
    for i in range(len(array)):
        if curSum <= 0:
            curSum = array[i]
        else:
            curSum += array[i]
        
        if curSum > maxSum:
            maxSum = curSum
    
    return maxSum

if __name__ == "__main__":
    arr = [-1,-2,-3]
    print(findGreatestSum(arr))