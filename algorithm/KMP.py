#coding:utf-8



'''
说明：kmp算法


'''

def get_next(p):
    p_len = len(p)
    i, j = 0, -1
    next[0] = -1
    while i < p_len-1:
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
    return next

def kmp(s,p):
    slen, plen = len(s), len(p)
    if slen >= plen:
        i, j = 0, 0
        next = getnext(p)
        while i < slen:
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = next[j]
            if j == plen:
                return j - plen
    return -1
