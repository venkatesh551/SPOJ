'''
Created on 08-Jun-2015

@author: Venkatesh
'''


def read_int():
    return int(raw_input())


def count_distinct_strings(inp_str):
    all_substrings = set()
    n = len(inp_str)
    for i in xrange(n):
        for j in xrange(i, n):
            all_substrings.add(inp_str[i:j+1])
    return len(all_substrings)


def main():
    tc = read_int()
    for _ in xrange(tc):
        inp_str = raw_input()
        print count_distinct_strings(inp_str)


if __name__ == '__main__':
    main()
