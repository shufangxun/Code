def findMinNumber(array):
    ## 将数组元素拼接成一个数，找出最小的数
    ## 为避免溢出，变为字符操作
    ## 运行时间：27ms
    ## 占用内存：5860k
    if len(array) == 0:
        return ''

    num2str = [str(n) for n in array]
    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):  ## i+1
            if num2str[i] + num2str[j] > num2str[j] + num2str[i]: ## 字符串比较 ASCII 长度一样
                num2str[i], num2str[j] = num2str[j], num2str[i]
    
    return ''.join(num2str)  ## 去掉空格

if __name__ == "__main__":
    arr = [4,3,2,1]
    print(findMinNumber(arr))