class BohrNode:
    def __init__(self, parent, new_letter):
        self.sub = parent + new_letter
        self.parent = parent
        self.len = len(self.sub)
        self.suffix = ''
        self.heirs = []


def aho_corasick(text, sub):
    if sub == '':
        return 0
    bohr = _build_dfa(sub)
    current = bohr['']
    for i in range(len(text)):
        e = text[i]
        while e not in current.heirs:
            if current.sub == '':
                break
            current = bohr[current.suffix]
        else:
            current = bohr[current.sub + e]
            if current.sub == sub:
                return i - current.len + 1
    return -1
            
    
def _build_dfa(sub):
    tree = dict()
    tree[''] = BohrNode('', '')
    current = tree['']
    for e in sub:
        new_sub = current.sub + e
        tree[new_sub] = BohrNode(current.sub, e)
        current.heirs.append(e)
        current = tree[current.suffix]
        while current.sub != '':
            if e in current.heirs:
                tree[new_sub].suffix = current.sub + e
                break
            else:
                current = tree[current.suffix]
        current = tree.get(new_sub)
    return tree
