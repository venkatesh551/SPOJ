'''
Created on 11-Jun-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def calculate_all_values():
    result = [0]
    init_seq = [1] * 10
    for _ in xrange(1, 65):
        total = sum(init_seq)
        result.append(total)
        cur_val, init_seq[0] = init_seq[0], total
        for ind in xrange(1, len(init_seq)):
            prev_val = init_seq[ind]
            init_seq[ind] = init_seq[ind-1] - cur_val
            cur_val = prev_val
    return result


def main():
    values = calculate_all_values()
    tc = read_int()
    for _ in xrange(tc):
        seq, n = read_int_list()
        print seq, values[n]


if __name__ == '__main__':
    main()
