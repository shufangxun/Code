import collections
def reorderArray1(array):
    ##将数组的奇数置前，偶数置后，保持元素间的相对位置   
    '''
    solution 1
    sorted(iterable,key,reverse=False) 默认是升序
    运行时间：24ms
    占用内存：5624k   
        '''
    return sorted(array, key=lambda x:x%2==0)

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(reorderArray1(arr))   
