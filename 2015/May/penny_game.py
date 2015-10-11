'''
Created on 20-Sep-2015

@author: venkat
'''

from collections import defaultdict


all_comb = ["TTT", "TTH", "THT", "THH",
            "HTT", "HTH", "HHT", "HHH"
            ]


def read_int():
    return int(raw_input())


def count_all_comb(in_str):
    cnt_d = defaultdict(int)
    for ind in xrange(38):
        substr = in_str[ind:ind+3]
        cnt_d[substr] += 1
    for ele in all_comb:
        print cnt_d[ele],


def main():
    tc = read_int()
    for _ in xrange(tc):
        tc_num = read_int()
        in_str = raw_input()
        print tc_num,
        count_all_comb(in_str)


if __name__ == '__main__':
    main()
