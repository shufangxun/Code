def duplicate1(array, duplication = []):
    ## 返回任意一个重复数组，条件很松
    '''
        数组元素个数为n,范围[0,n-1],找到重复的元素
        先排序,后遍历,当相邻元素一样时，重复
        时间复杂度 O(nlogn)
        运行时间：25ms
        占用内存：5724k
        '''
    orderArr = sorted(array) ## 升序
    for i in range(1, len(orderArr)):  ## 防止数组溢出
        if orderArr[i - 1] == orderArr[i]:
            duplication.append(orderArr[i])
            return True
    return False

if __name__ == "__main__":
    arr = [1,2,3,2]
    print(duplicate1(arr))


