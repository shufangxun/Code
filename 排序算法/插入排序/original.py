def insertsort(arr):
    for i, item in enumerate(arr):
        j = i
        # 从右往左插入
        while j > 0 and arr[j - 1] > item:
            arr[j] = arr[j - 1]
            index -= 1
        arr[j] = item
    return arr

if __name__ == "__main__":
    a = [2,1,2,3]
    print(insertsort(a))
