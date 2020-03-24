# 二分法
# 递归
def pow1(x, n):
    if n == 0: return 1
    if n == 1: return x
    if n == -1: return 1 / x

    half = pow(x, n // 2)
    
    if n & 1 == 0:
        return  half * half 
    else:
        return half * half * x

# 非递归
def myPow(x, n):
    if n < 0:
        n = - n
        x = 1 / x 
    
    res = 1
    while n:
        if n & 1: # 若指数是奇数，才会乘上去
            res = res * x
        x *= x
        n = n >> 1
    return res