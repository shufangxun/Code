
# solution 1
# import collections
# a=[1,2,3,1,2]
# print([item for item,count in collections.Counter(a).items() if count > 1])


def countDuplicate(array):
    unique = set(array)
    for i in unique:
        count = 0
        for j in array:
            if i == j:
                count += 1
        print(i,":",count)

if __name__ == "__main__":
    arr = [1,2,3,2,1,4,4,3]
    print(countDuplicate(arr))