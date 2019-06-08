def duplicate2(array, duplication = []):
    '''
        hash法 开辟空间存数组，当hash table内没有时，数目+1，否则输出
        时间复杂度： O(n)
        空间复杂度： O(n)
        运行时间：28ms
        占用内存：5752k
        '''
    hashmap = [0] * len(array)  ## 开辟一个空间，其实有浪费，有些没用到

    for i in range(len(array)):
        if hashmap[array[i]] == 0: ## 对应元素不存在
            hashmap[array[i]] = 1
        else:
            duplication.append(array[i])
            # return True
    print(duplication)
    # return False

if __name__ == "__main__":
    arr = [30,1,30,3,3,4]
    print(duplicate2(arr))
