'''
Created on 29-Sep-2015

@author: venkat
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def main():
    n = read_int()
    degree = [0] * (n + 1)
    for _ in xrange(1, n):
        a, b = read_int_list()
        degree[a] += 1
        degree[b] += 1
    degree.sort(reverse=True)
    cnt, idx = 0, 0
    while idx < n and cnt < n-1:
        cnt += degree[idx]
        idx += 1
    print idx

if __name__ == '__main__':
    main()
