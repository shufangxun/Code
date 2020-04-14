def bottomup_mergesort(arr):
    length = len(arr)
    size = 1
    while size < length:
		size *= 2
		for pos in range(0, length, size):
			sublist_start = pos
			sublist_mid   = pos + (size / 2)
			sublist_end = pos + size
			left  = list[ sublist_start : sublist_mid ]
			right = list[   sublist_mid : sublist_end ]
			list[sublist_start:sublist_end] = merge(left, right)
    return list
    
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
