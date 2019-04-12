def duplicate3(array, duplication = []):
    '''
        hash法 
        [i] = m ,[m] = n
        若i == m,考察i + 1；若i != m,考察m和n
        若m == n,则为重复元素，否则，交换m和n,即[i] = n,[m] = m,重复判断[i]--用while 
        时间复杂度： O(n)
        空间复杂度： O(1)
        运行时间：23ms
        占用内存：5732k
        '''
    for i in range(len(array)):
        while array[i] != i:  ## 这边重复操作
            if array[array[i]] == array[i]:
                duplication.append(array[i])
                return True
            else:
                array[array[i]], array[i] = array[i], array[array[i]]
    return False


if __name__ == "__main__":
    arr = [2,1,3,1,4]
    print(duplicate3(arr))
