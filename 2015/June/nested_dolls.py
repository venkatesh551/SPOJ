'''
Created on 23-Jun-2015

@author: Venkatesh

MDOLLS - Nested Dolls

'''


def read_pairs():
    num_lst = [int(x) for x in raw_input().split()]
    it = iter(num_lst)
    return [(ele, next(it)) for ele in it]


def read_int():
    return int(raw_input())


def min_no_of_nested_dolls(all_pairs, n):
    all_pairs.sort()
    ans = 1
    for ind in xrange(1, n):
        if all_pairs[ind][0] <= all_pairs[ind-1][0] or \
           all_pairs[ind][1] <= all_pairs[ind-1][1]:
            ans += 1
    return ans


def main():
    tc = read_int()
    for _ in xrange(tc):
        n = read_int()
        all_pairs = read_pairs()
        print min_no_of_nested_dolls(all_pairs, n)


if __name__ == '__main__':
    main()
