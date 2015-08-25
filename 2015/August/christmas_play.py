'''
Created on 21-Aug-2015

@author: venkatesh
'''


def read_int():
    return int(raw_input())


def read_list(func):
    return [func(x) for x in raw_input().split()]


def get_max_elements(a_lst, n, k):
    return [max(a_lst[ind:ind+k]) for ind in xrange(0, n-k+1)]


def get_min_diff(a_lst, n, k):
    a_lst.sort()
    ans = 1000000000
    for ind in xrange(0, n-k+1):
        ans = min(a_lst[ind + k - 1] - a_lst[ind], ans)
    return ans


def main():
    tc = read_int()
    for _ in xrange(tc):
        n, k = read_list(int)
        a_lst = read_list(int)
        print get_min_diff(a_lst, n, k)

if __name__ == '__main__':
    main()
