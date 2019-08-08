# 扩展 输出最长字符串
def longestSubstringWithoutDuplication(s):
    """
    :type s: str
    :rtype: int
    """
    left = 0
    curlen = maxlen = 0
    a_list = []
    lookup = set()
    for i in range(len(s)):
        a = {}
        curlen += 1
        while s[i] in lookup:
            lookup.remove(s[left])
            left += 1
            curlen -= 1
        if curlen > maxlen:maxlen = curlen
        lookup.add(s[i])
        a[curlen] = list(lookup) 
        a_list.append(a) 
    for key in a_list:
        for i in key:
            if i == maxlen:
                print ("===================",key[i])
    return maxlen
