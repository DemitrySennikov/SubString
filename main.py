from brute_force import brute_force
from rabin_karp import rabin_karp
from kmp import kmp
from aho_corasick import aho_corasick
from bmh import bmh
from graphics import draw_all_graphs


def main(text, sub):
    print(f"Searching '{sub}' in '{text}':")
    print("Brute Force:", brute_force(text, sub))
    print("Rabin-Karp:", rabin_karp(text, sub))
    print("Aho-Corasick:", aho_corasick(text, sub))
    print("Knuth-Morris-Pratt:", kmp(text, sub))
    print("Boyer–Moore–Horspool:", bmh(text, sub))
    print("Correct:", text.index(sub))
    draw_all_graphs()
    
    
if __name__ == '__main__':
    main('acbcbcaabcaabc', 'bca')
