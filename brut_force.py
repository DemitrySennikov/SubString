def brut_force(text, sub):
    n = len(text)
    s = len(sub)
    for start in range(n-s+1):
        for x in range(s):
            if text[start+x] != sub[x]:
                break
        else:
            return start
    return -1
