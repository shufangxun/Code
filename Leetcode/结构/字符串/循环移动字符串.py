def rotateString(s, offset):
    if not s:
        return s
    offset = offset % len(s)
    reverse(s, 0, offset - 1)
    reverse(s, offset, len(s) - 1)
    reverse(s, 0, len(s) - 1)
    return s
    
def reverse(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1 
        end -= 1 

if __name__ == "__main__":
    s = list("abcdefg")
    n = 2
    s = rotateString(s, n)
    print(s)