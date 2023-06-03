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
            current_hash = _update_sub_hash(s, current_hash, 
                                            text[start], text[start + s])
    return -1
    
    
def _get_hash_code(text):
    hash = 0
    for e in text:
        hash = 397*hash + ord(e)
    return hash


def _update_sub_hash(sub_len, hash, old_e, new_e):
    return (hash - ((397 ** (sub_len-1))*ord(old_e)))*397 + ord(new_e)
