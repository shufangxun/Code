def m(matrix):
    m, n = len(matrix), len(matrix[0])
    total = [[0] * n for _ in range(m+1)]
    maxSum = 0
    # 计算前缀和 特殊处理第一行
    for i in range(m+1):
        for j in range(n):
            if i == 1:
                total[i][j] = matrix[i-1][j]
            if i >= 2:
                total[i][j] = total[i - 1][j] + matrix[i-1][j]
    return total

ma = list([[1,3,-1],[2,3,-2],[-1,-2,-3]])
a = m(ma)
print(ma)
print(a)