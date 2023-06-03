from brut_force import brut_force
from rabin_karp import rabin_karp
from kmp import kmp
from aho_korasik import aho_korasik

def test(text, sub):
    print("Searching", sub, "in", text, ":")
    print("Brut Force:", brut_force(text, sub))
    print("Rabin-Karp:", rabin_karp(text, sub))
    print("Aho-Korasik:", aho_korasik(text, sub))
    print("Knuth-Morris-Pratt:", kmp(text, sub))
    print("Correct:", text.index(sub))
    print()
    
    
if __name__ == '__main__':
    test('acbcbcaabcaabc', 'bca')