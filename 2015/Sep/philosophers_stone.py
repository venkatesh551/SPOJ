'''
Created on 29-Sep-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def read_tbl(n):
    return [read_int_list() for _ in xrange(n)]


def max_path_value(mat, n, m):
    for ele in mat:
        ele.insert(0, 0)
        ele.append(0)
    # print mat
    for i in xrange(1, n):
        for j in xrange(1, m+1):
                mat[i][j] += max(mat[i-1][j], mat[i-1][j+1], mat[i-1][j-1])
    return max(mat[n-1])


def main():
    tc = read_int()
    for _ in xrange(tc):
        n, m = read_int_list()
        mat = read_tbl(n)
        print max_path_value(mat, n, m)

if __name__ == '__main__':
    main()
