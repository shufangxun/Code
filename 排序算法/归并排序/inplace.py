def merge(list, temp, low, mid, high):
    	'''
	Merges two sorted halves of a list in order.
	'''
	for z in range(low, high+1):
		temp[z] = list[z] # copy items into temp
	
	first = low  # position in 1st half
	sec   = mid + 1	 # position in 2nd half
	
	for z in range(low, high+1):
		if first > mid: # if past the end of 1st half,
			list[z] = temp[sec]	# add next value of 2nd half
			sec+=1

		elif sec > high: # if past the end of 2nd half,
			list[z] = temp[first] # add value from 1st half,
			first+=1

		elif temp[sec] < temp[first]: # if value in 2nd < value in 1st,
			list[z] = temp[sec] # add value from 2nd half,
			sec+=1
		
		else: # if value in 1st < value in 2nd,
			list[z] = temp[first] # add next value in 1st half,
			first+=1 # imcrement first

def sort(list, temp, low, high):
	if high <= low:
		return # stop recursion
	mid = low + (high - low) / 2 # calculate mid between high and low
	sort(list, temp, low, mid) # recursive sort the first half
	sort(list, temp, mid+1, high) # recursive sort the second half
	merge(list, temp, low, mid, high) # merge the two halves
	
def mergesort(list):
	length = len(list)
	temp = [0] * length
	sort(list, temp, 0, length-1)
	
def bottomup_mergesort(list):
	length = len(list)
	temp = [0] * length
	size = 1
	while size < length:
		pos = 0
		while pos < length:
			if (pos+2*size-1 >= length):
				merge(list, temp, pos, pos+size-1, length-1)
			else:
				merge(list, temp, pos, pos+size-1, pos+2*size-1)
			pos+=2*size
		size+=size
	return