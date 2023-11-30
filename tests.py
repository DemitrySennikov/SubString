import unittest

from brute_force import brute_force
from kmp import kmp
from rabin_karp import rabin_karp
from aho_corasick import aho_corasick
from bmh import bmh

from random import choice
from string import ascii_letters

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.test_cases_with_sub = [('abc', 'abc'),
                                    ('abcskcndlsvkdnvln', 'abc'),
                                    ('vnjkjhkdabcdvjldd', 'abc'),
                                    ('lvhdlvdlvdlvrvabc', 'abc'),
                                    ('lffabcfkbnlmvabcf', 'abc'),
                                    ('lvnslfabcabcabcmdl', 'abcab'),
                                    ('aaaaaaaaaaaaaaa', 'a'),
                                    ('aaaaaaaaaaaaaaa', 'aaa'),
                                    ('abababababab', 'bab')]
        self.test_cases_without_sub = [('ldvnnlfngdffvsd', 'abc'),
                                       ('abababababab', 'abc'),
                                       ('aabaabaabaabaa', 'aaa'),
                                       ('d', 'abc'),
                                       ('abc', 'def')]
        
    def _method_testing(self, method):
        for text, sub in self.test_cases_with_sub:
            self.assertEqual(method(text, sub), text.index(sub))
        for text, sub in self.test_cases_without_sub:
            self.assertEqual(method(text, sub), -1)
        for x in range(100):
            text = ''.join(choice(ascii_letters) for _ in range(1000*x))
            sub = ''.join(choice(ascii_letters) for _ in range(100))
            if sub in text:
                self.assertEqual(method(text, sub), text.index(sub))
            else:
                self.assertEqual(method(text, sub), -1)

    def test_brute_force(self):
        self._method_testing(brute_force)
        
    def test_kmp(self):
        self._method_testing(kmp)

    def test_rabin_karp(self):
        self._method_testing(rabin_karp)

    def test_aho_corasick(self):
        self._method_testing(aho_corasick)

    def test_bmh(self):
        self._method_testing(bmh)

if __name__ == "__main__":
    unittest.main()
