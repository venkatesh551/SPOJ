from collections import defaultdict


def read_int():
	return int(raw_input())


def read_list(func):
    return [func(x) for x in raw_input().split()]


def print_major_element(a_lst):
    n = len(a_lst)
    d = defaultdict(int)
    for ele in a_lst:
        d[ele] += 1
    for key, val in d.iteritems():
        if val > n/2:
            print "YES", key
            return
    print "NO"        


def main():
    tc = read_int()
    for _ in xrange(tc):
        _ = read_int()
        a_lst = read_list(int)
        print_major_element(a_lst)


if __name__ == '__main__':
    main()
