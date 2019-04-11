def countK(array, K):
    '''
        思路：找到第一个K和最后一个K的索引，因为是有序数组，即可得到K的数目
        方法：利用二分查找，首先查看中位数是否是第一个，若比K小，在后半段找K， 
              若比K大，在前半段找K，若正好等于K，判断前面一个是否为K，若不是则是第一个K，
              若是，则在前半段
        '''
    if not array:
        return 0
    
    firstIndex = firstK(array, K)
    lastIndex = lastK(array, K)
    if firstIndex == -1 and lastIndex == -1:
        return 0
    else:
        return lastIndex - firstIndex + 1


def firstK(array, K):
    front = 0
    rear = len(array) - 1
    while front <= rear:
        mid = (front + rear) // 2
        if array[mid] > K:
            rear = mid - 1
        elif array[mid] < K:
            front = mid + 1
        else:  ## array[mid] = K
            if mid == front or array[mid - 1]!=K:
                return mid
            else: ## array[mid - 1] == K
                rear = mid - 1
        
    return -1


def lastK(array, K):
    front = 0
    rear = len(array) - 1
    while front <= rear:
        mid = (front + rear) // 2
        if array[mid] < K:      ## 这里和找第一个一样，只是当[mid] == K 不同
            front = mid + 1
        elif array[mid] > K:
            rear = mid - 1
        else:  ## array[mid] = K
            if mid == rear or array[mid + 1]!=K:  ## 先判断前面，后面这个有可能溢出报错
                return mid
            else: ## array[mid - 1] == K
                front = mid + 1
        
    return -1

if __name__ == "__main__":
    arr = [1,1,1,3,3]
    print(countK(arr,1))