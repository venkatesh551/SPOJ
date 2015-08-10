'''
Created on 06-Aug-2015

@author: Venkatesh

problem : JNEXT - Just Next !!!

'''


def read_str_list():
    return [x for x in raw_input().split()]


def read_int():
    return int(raw_input())


def get_next_number(digits):
    pos = None
    d_len = len(digits)
    for ind in xrange(d_len-2, -1, -1):
        if digits[ind] < digits[ind+1]:
            pos = ind
            break
    # print pos
    if pos is None:
        return -1
    digits[pos+1:d_len] = sorted(digits[pos+1:d_len])
    for i in xrange(pos+1, d_len):
        if digits[pos] < digits[i]:
            digits[pos], digits[i] = digits[i], digits[pos]
            break
    return "".join(digits)


def main():
    tc = read_int()
    for _ in xrange(tc):
        _ = read_int()
        digits = read_str_list()
        print get_next_number(digits)


if __name__ == '__main__':
    main()
