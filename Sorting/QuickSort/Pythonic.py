def QuickSort1(array):
    '''
        非常python的写法
        分治：
        1.定基
        2.分区
        3.递归调用上面两步，直到front >= rear
        
        '''
    if len(array) <= 1:
        return array
    else:
        pviot = array[0]
        return QuickSort1([x for x in array[1:] if x < pviot]) + [pviot] + \
            QuickSort1([x for x in array[1:] if x >= pviot])

if __name__ == "__main__":
    arr = [5,4,3,7,8,3,1]
    print(QuickSort1(arr))