def kmp(text, sub):
    offset = _offset_list(sub)
    s = len(sub)
    current = 0
    prefix_counter = 0
    while prefix_counter != s:
        if text[current] == sub[prefix_counter]:
            prefix_counter += 1
        elif prefix_counter != 0:
            prefix_counter = offset[prefix_counter]
            continue
        current += 1
        if current == len(text) and prefix_counter < s:
            return -1
    else:
        return current - s


def _offset_list(sub):
    result = [0 for _ in range(len(sub))]
    prefix_counter = 0
    for current in range(2, len(sub)):
        while sub[current-1] != sub[prefix_counter]:
            if prefix_counter == 0:
                break
            prefix_counter = result[prefix_counter]
        else:
            prefix_counter += 1
            result[current] = prefix_counter
    return result
