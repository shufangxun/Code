def matrix_multiply(A, B):
    '''
    矩阵乘法
    '''
    m, p = len(A), len(A[0])
    n = len(B[0])
    if p != len(B):
        raise ValueError("A和B维度不匹配")
    C = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == "__main__":
    A = [[1,2,3],[1,2,3],[4,5,6]]
    B = [[1,2,3,0],[1,2,3,1],[4,5,6,9]]
    print(matrix_multiply(A,B))