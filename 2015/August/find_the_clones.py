'''
Created on 16-Aug-2015

@author:  Venkatesh
'''

from collections import defaultdict


def read_int_list():
    return [int(x) for x in raw_input().split()]


def main():
    while True:
        n, _ = read_int_list()
        if n == 0:
            return
        dna_seq_dict = defaultdict(int)
        for _ in xrange(n):
            inp = raw_input()
            dna_seq_dict[inp] += 1
        result = [0 for _ in xrange(n+1)]
        for val in dna_seq_dict.values():
            result[val] += 1
        result.pop(0)
        for ele in result:
            print ele


if __name__ == '__main__':
    main()
