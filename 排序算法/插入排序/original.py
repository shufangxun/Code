def insertsort(arr):
    for i, item in enumerate(arr):
        index = i
        while index > 0 and arr[index - 1] > item:
            arr[index] = arr[index - 1] 
            index -= 1
        
        arr[index] = item
    
    return arr


if __name__ == "__main__":
    a = [2,1,2,3]
    print(insertsort(a)) 
