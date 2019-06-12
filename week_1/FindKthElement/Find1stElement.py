def findElement1st1(array):
    ## 两个元素出现一次，其余都是两次，找出这两个元素
    '''
        input:{2,4,3,6,3,2,5,5}
        output:{4,6}
        引例：若只有一个元素出现一次，其余都是两次？
              因为a XOR a = 0，所以逐元素异或即可
        思路：首先逐元素异或，得到两个单元素异或的值，因为两个元素当位不同时XOR为1，所以找第一个位数为1的位置，
            以此位划分数组，最后对划分的数组分别进行逐元素异或
            ^: 异或
        运行时间：25ms
        占用内存：5624k
        '''
    # step 1
    xor = 0
    for i in array:
        xor ^= i

    # step 2
    idxof1 = 0 
    while xor & 1 == 0 and idxof1 < 32: # 这个1是00000001
        idxof1 += 1
        xor = xor >> 1 # 右移一位
       
    
    # step 3
    num1, num2 = 0, 0
    for j in array:
        if ((j >> idxof1) & 1) == 1:  # 看对应位是否为1，分类操作
            num1 ^= j
        else:
            num2 ^= j

    return [num1, num2]
      


def findElement1st2(array):
    '''
        通过hashmap统计
        时间复杂度：O(n)
        空间复杂度：O(n)
        运行时间：22ms
        占用内存：5752k
        '''
    hashmap = {}
    for i in array:
        if str(i) in hashmap:    ## 当key存在时，+1
            hashmap[str(i)] += 1
        else:
            hashmap[str(i)] = 1
    
    result = []
    for key in hashmap.keys():
        if hashmap[key] == 1:
            result.append(int(key))
    return result



if __name__ == "__main__":
    arr = [2,4,3,6,3,2,5,5]
    print(findElement1st2(arr))
    print(findElement1st1(arr))

        
    
