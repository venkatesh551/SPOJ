'''
Created on 21-Sep-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def main():
    tc = read_int()
    for case in xrange(tc):
        need, n = read_int_list()
        nums = read_int_list()
        nums.sort(reverse=True)
        ind = 0
        while need > 0 and ind < n:
            need -= nums[ind]
            ind += 1
        print "Scenario #" + str(case+1) + ":"
        print "impossible" if need > 0 else ind


if __name__ == '__main__':
    main()
