def bubblesort(arr):
    
    for i in range(len(arr)): # 外层循环 比较多少轮
        swap = False # 没有交换设置为False
        for j in range(len(arr) - 1 - i): # 内存循环 每一轮的交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        
        if swap == False:
            break

    return arr
if __name__ == "__main__":
    a = [2,1,2,3]
    print(bubblesort(a)) 
