def distinctsubS(s):
    # 保持相对顺序
    end = [0] * 26
    for c in S:
        end[ord(c) - ord('a')] = sum(end) + 1
    return sum(end) % (10**9 + 7)