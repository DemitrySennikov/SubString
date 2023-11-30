def rabin_karp(text, sub):
    sub_hash = _get_hash_code(sub)
    n = len(text)
    s = len(sub)
    current_hash = _get_hash_code(text[:s])
    for start in range(n-s+1):
        if sub_hash == current_hash:
            for i in range(s):
                if text[start+i] != sub[i]:
                    break
            else:
                return start
        elif start + s < n:
            current_hash = _get_hash_code(text[start+1:start+s+1])
    return -1
    
    
def _get_hash_code(text):
    hash = 0
    for e in text:
        hash = (31*hash + ord(e))%(5)
    return hash

