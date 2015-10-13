'''
Created on 13-Oct-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def min_steps_to_reach(a, visted, start, end):
    if start > end or start < 0:
        return 2 * end
    if start == end:
        return 0
    visted[start] = True
    next_loc = start + a[start]
    if next_loc >= 0 and next_loc <= end and not visted[next_loc]:
        x = min_steps_to_reach(a, visted, next_loc, end)
    else:
        x = 2 * end
    next_loc = start+1
    if next_loc <= end and not visted[next_loc]:
        y = min_steps_to_reach(a, visted, next_loc, end)
    else:
        y = 2 * end
    visted[start] = False
    return 1 + min(x, y)


def main():
    tc = read_int()
    for _ in xrange(tc):
        n = read_int()
        a = read_int_list()
        visted = [False] * (n+1)
        print min_steps_to_reach(a, visted, 0, n)


if __name__ == '__main__':
    main()
