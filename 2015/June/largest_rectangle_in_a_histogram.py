'''
Created on 03-Jun-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def largest_rect_area(hist_seq):
    pass


def main():
    while True:
        hist_seq = read_int_list()
        if hist_seq[0] == 0:
            return
        else:
            print largest_rect_area(hist_seq)

if __name__ == '__main__':
    main()
