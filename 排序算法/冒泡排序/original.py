def bubblesort(arr):

    for i in range(len(arr)): # 外层循环 比较多少轮
        for j in range(len(arr) - 1 - i): # 内存循环 每一轮的交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

if __name__ == "__main__":
    a = [3,3,1,4]
    print(bubblesort(a))