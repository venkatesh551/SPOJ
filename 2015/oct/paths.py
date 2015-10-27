'''
Created on 14-Oct-2015

@author: Venkatesh
'''


def pre_calculate(m=15):
    tbl = []
    for i in xrange(m):
        tbl.append([1]*m)
    for i in xrange(1, m):
        for j in xrange(1, m):
            tbl[i][j] = tbl[i-1][j] + tbl[i][j-1]
    return tbl


def read_int():
    return int(raw_input())


def main():
    tbl = pre_calculate()
    tc = read_int()
    for _ in xrange(tc):
        n = read_int()
        print tbl[n][n]


if __name__ == '__main__':
    main()
