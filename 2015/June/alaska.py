'''
Created on 17-Jun-2015

@author: Venkatesh
'''


def read_int():
    return int(raw_input())


def is_possible(ele_lst):
    ele_lst.sort()
    init = 0
    for ele in ele_lst:
        if init < ele:
            return False
        else:
            init = 200 + ele
    diff = abs(init - 1422)
    return True if diff >= 100 else False


def main():
    while True:
        n = read_int()
        if n == 0:
            return
        ele_lst = []
        for _ in xrange(n):
            ele_lst.append(read_int())
        print "POSSIBLE" if is_possible(ele_lst) else "IMPOSSIBLE"


if __name__ == '__main__':
    main()
