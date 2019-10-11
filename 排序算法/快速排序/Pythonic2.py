from timeit import timeit
from random import random

def Quicksort3(array):
    less = []
    equal = []
    greater = []
    
    if len(array) > 1:
        pviot = array[0]
        for x in array:
            if x < pviot:
                less.append(x)
            elif x == pviot:
                equal.append(x)
            else:
                greater.append(x)
        return Quicksort3(less) + equal + Quicksort3(greater)
    else:
        return array

if __name__ == "__main__":
    randomList = [random() for num in range(1_000)]
    time2 = timeit('Quicksort3(randomList)', globals=globals(), number=100)  ## 随机定义100个数
    print('Quicksort3: ' + str(time2))