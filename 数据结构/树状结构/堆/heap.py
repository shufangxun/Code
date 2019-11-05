# 以最小堆为例
def push(x, heap):
    heap.append(x)
    shiftup1(heap, len(heap)-1)

# 上浮
#1. 基于迭代
def shiftup(heap, i):
    p = (i - 1) // 2
    while p >= 0: # 保证父节点
        if heap[i] < heap[p]:
            heap[i], heap[p] = heap[p], heap[i]
            i, p = p, (p - 1) // 2
        else:
            break

#2. 基于递归
def shiftup1(heap, i):
    p = (i - 1) // 2
    if p >= 0 and heap[i] < heap[p]:
        heap[i], heap[p] = heap[p], heap[i]
        shiftup(heap, p)



'''
下沉操作
'''
def shiftdown(heap, i):
    # small_child = -1
    while 2 * i <= len(heap) - 1:
        l = 2 * i + 1
        r = 2 * i + 2
        if l <= len(heap) - 1: # 左孩子未越界
            small_child = l
        if r <= len(heap) - 1 and heap[r] < heap[l]: # 右孩子未越界 & 右孩子小于左孩子
            small_child = r
        if heap[i] > heap[small_child]:
            heap[i], heap[small_child] = heap[small_child], heap[i]
            i = small_child
        else:
            break

def shiftdown1(heap, i):
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= len(heap) - 1: # 左孩子未越界
        small_child = l
    if r <= len(heap) - 1 and heap[r] < heap[l]: # 右孩子未越界
        small_child = r
    if heap[i] < heap[small_child]:
        heap[i], heap[small_child] = heap[small_child], heap[i]
        shiftdown(heap, small_child)

def delet(heap):
    heap[0], heap[-1] = heap[-1], heap[0] # 交换
    heap.pop(-1) # 移除最后一个元素
    shiftdown(heap, 0)

def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1 , -1, -1):
        shiftdown(arr, i)

def heapsort(arr):
    build_heap(arr)
    ans = []
    while len(arr) > 0:
        ans.append(arr[0])
        arr[0], arr[len(arr)-1] = arr[len(arr)-1], arr[0]
        arr.pop()
        shiftdown(arr, 0)
    ans.append(arr[0])
    return ans

if __name__ == "__main__":
    c = [9,5,3,1,6,7,3,10,8]
    build_heap(c)
    print('constructed heap:', c)
    delet(c)
    print('deleted root:', c)
    push(2,c)
    print('add to heap:', c)
    ans = heapsort(c)
    print('heapsort:', ans)
