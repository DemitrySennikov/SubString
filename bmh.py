def bmh(text, sub):
    shifts = _shifts(sub)
    start = 0
    while start + len(sub) <= len(text):
        for i in range(len(sub)):
            if sub[i] != text[start+i]:
                if text[start+len(sub)-1] in shifts:
                    start += shifts[text[start+len(sub)-1]]
                else:
                    start += len(sub)
                break
            if i == len(sub) - 1:
                return start
    return -1


def _shifts(sub):
    shifts = dict()
    for i in range(len(sub) - 1):
        shifts[sub[i]] = len(sub) - i - 1
    return shifts
