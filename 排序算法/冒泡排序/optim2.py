def bubblesort(arr):
    
    swap = True
    while swap:
        swap = False # 没有交换设置为False
        i = 0 # 已排序标签
        for j in range(len(arr) - 1 - i): # 内存循环 每一轮的交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
            i += 1
  
    return arr

if __name__ == "__main__":
    a = [2,1,2,3]
    print(bubblesort(a)) 