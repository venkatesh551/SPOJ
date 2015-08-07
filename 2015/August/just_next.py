'''
Created on 06-Aug-2015

@author: Venkatesh

problem : JNEXT - Just Next !!!

'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def next_number_exists(digits):
    for ind in xrange(1, len(digits)):
        if digits[ind] > digits[ind-1]:
            return True
    return False


def get_next_number(digits):
    if not next_number_exists(digits):
        return -1
    


def main():
    tc = read_int()
    for _ in xrange(tc):
        _ = read_int()
        digits = read_int_list()
        print get_next_number(digits)


if __name__ == '__main__':
    main()
