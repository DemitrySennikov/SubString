from brute_force import brute_force
from kmp import kmp
from rabin_karp import rabin_karp
from aho_corasick import aho_corasick
from bmh import bmh

import time
import tracemalloc
import matplotlib.pyplot as plt

from random import choice
from string import ascii_letters


def draw_graphs(method):
    y_time =  []
    y_memory = []
    x = [i for i in range(10000, 100001, 10000)]

    for i in x:
        print(i)
        time_sum = 0
        memory_sum = 0

        for j in range(1, i, i//10):
            text = ''.join(choice(ascii_letters) for _ in range(i))
            sub = ''.join(choice(ascii_letters) for _ in range(j))
            tracemalloc.start()
            start_time = time.time()
            method(text, sub)
            end_time = time.time()
            memory_sum += tracemalloc.get_traced_memory()[1]
            time_sum += (end_time - start_time) * 1000
            tracemalloc.reset_peak()
        
        y_memory.append(memory_sum)
        y_time.append(time_sum)
    
    y_memory = [y - min(y_memory) for y in y_memory]

    plt.subplot(2, 1, 1)
    plt.plot(x, y_time, label=method.__name__)
    plt.xlabel('Text Length')
    plt.ylabel('Time')
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.plot(x, y_memory, label=method.__name__)
    plt.xlabel('Text Length')
    plt.ylabel('Memory')
    plt.legend()

    plt.show()

def draw_all_graphs():
    methods = [brute_force, rabin_karp, kmp, aho_corasick, bmh]
    for method in methods:
        draw_graphs(method)

