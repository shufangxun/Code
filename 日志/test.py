def lastRemaining(n, m):
    """
    :type n: int
    :type m: int
    :rtype: int
    """
    if n == 1:
        return 0
    else:
        return (lastRemaining(n - 1, m) + m) % n


if __name__ == "__main__":
    n, m = 10, 3
    s = lastRemaining(n,m)
    print(s)