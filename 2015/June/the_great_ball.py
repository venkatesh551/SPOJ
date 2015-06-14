'''
Created on 14-Jun-2015

@author: venkat
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def max_no_of_dancers_in_interval(s_lst, e_lst):
    s_lst.sort()
    e_lst.sort()
    n = len(s_lst)
    i, j = 0, 0
    cnt, ans = 0, 0
    while i < n and j < n:
        if s_lst[i] < e_lst[j]:
            cnt += 1
            i += 1
        else:
            cnt -= 1
            j += 1
        ans = max(ans, cnt)
    return ans


def main():
    tc = read_int()
    for _ in xrange(tc):
        n = read_int()
        s_lst = []
        e_lst = []
        for _ in xrange(n):
            start, end = read_int_list()
            s_lst.append(start)
            e_lst.append(end)
        print max_no_of_dancers_in_interval(s_lst, e_lst)

if __name__ == '__main__':
    main()
