def selectsort(arr):

    for i in range(len(arr)):
        min = i # 坐标
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr

if __name__ == "__main__":
    a = [2,1,3,2]
    print(selectsort(a))