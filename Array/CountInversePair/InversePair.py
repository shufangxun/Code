
def inversePair(array):
   ## 统计数组中的逆序数 leetcode-493
   '''
      归并法：
      这是归并排序的合并过程，考虑合并两个有序序列时，计算逆序对数。
      对于两个升序序列，设置两个下标：两个有序序列的末尾。每次比较两个末尾值，
      如果前末尾大于后末尾值，则有”后序列当前长度“个逆序对；否则不构成逆序对。
      然后把较大值拷贝到辅助数组的末尾，即最终要将两个有序序列合并到辅助数组并有序
      '''
   if not array:
    	return 0
   return mergeSort(array, 0, len(array) - 1)

def mergeSort(array, start, end):
   if start == end:
    	return 0

   count = 0
   mid = (start + end) // 2
   count += mergeSort(array, start, mid)
   count += mergeSort(array, mid + 1, end)
	
   left = start
   right = mid + 1
   while left <= mid and right <= end:
	   if array[left] > array[right]:
		   count += mid - left + 1
		   right += 1
	   else:
		   left += 1

   ## 此处有重复排序的问题，可以开辟空间存储		
   array[start : end + 1] = sorted(array[start : end + 1])
	
   return count

if __name__ == "__main__":
    arr = [3,4,1,2]
    print(inversePair(arr))
