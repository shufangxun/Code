# 枚举法
def compression(matrix, up, down, col):
    sum = 0
    for i in range(up, down + 1):
        sum += matrix[i][col]
    return sum

def maxSubmatrix1(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0 or matrix is None:
        return 0
    m, n = len(matrx), len(matrix[0])
    maxSum = 0
    for up in range(m):
        for down in range(up, m):
            curSum = 0
            # 连续子数组最大和
            for col in range(n):
                if curSum > 0:
                    curSum += compression(matrix, up, down, col)
                else:
                    curSum = compression(matrix, up, down, col)
                maxSum = max(maxSum, cuSum)
    return maxSum


# 预先存储1
class Solution1:
    def maxSubmatrix2(self, matrix):
        # write your code here
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m, n = len(matrx), len(matrix[0])
        maxSum = 0
        for up in range(m):
            sum = [0 for m in range(n)]
            for down in range(up, m):
                for col in range(n):
                    sum[col] += matrix[down][col]
                temp = self.maxSubarray(sum)
                maxSum = max(maxSum, temp)
        return maxSum

    def maxSubarray(self, array):
        res = 0
        sum = 0
        for i in range(0, len(array)):
            sum += array[i]
            res = max(res, sum)
            sum = max(sum, 0)
        return res

# 预先存储2
class Solution2:
    def maxSubmatrix(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        # 定义空间 注意第一行之前再定义一个全0行
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
        # 计算范围和
        for up in range(1, m+1):
            for down in range(up, m+1):
                curSum = 0
                for col in range(n):
                    if curSum >= 0:
                        curSum += total[down][col] - total[up-1][col]
                    else:
                        curSum =  total[down][col] - total[up-1][col]
                    maxSum = max(curSum, maxSum)
        return maxSum