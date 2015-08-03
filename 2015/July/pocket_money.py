'''
Created on 28-Jul-2015

@author: Venkatesh
'''


def read_int():
    return int(raw_input())


def get_value(in_str):
    pass


def main():
    tc = read_int()
    for _ in xrange(tc):
        in_str = raw_input()
        max_val, expr_val = get_value(in_str)
        print (max_val, expr_val)

if __name__ == '__main__':
    main()
