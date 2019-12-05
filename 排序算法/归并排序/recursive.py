def mergesort(arr):
    '''
    主函数入口
    1.先分后治，递归分数组，然后调用排序合并
       '''
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    merged = merge(left, right)   # 每次merge都要new一个数组空间, 消耗很大
    return merged

def merge(left, right):
    sorted = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    sorted += left[i:]
    sorted += right[j:]
    return sorted


if __name__ == "__main__":
    a = []
    print(mergesort(a))


    