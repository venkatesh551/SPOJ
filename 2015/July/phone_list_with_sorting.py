'''
Created on 30-Jul-2015

@author: Venkatesh
'''


def read_str_list(n):
    return [raw_input().rstrip() for _ in xrange(n)]


def read_int():
    return int(raw_input())


def main():
    tc = read_int()
    for _ in xrange(tc):
        n = read_int()
        s_lst = read_str_list(n)
        s_lst.sort()
        found = False
        for ind in xrange(1, n):
            if s_lst[ind].startswith(s_lst[ind-1]):
                found = True
                break
        print "NO" if found else "YES"

if __name__ == '__main__':
    main()
