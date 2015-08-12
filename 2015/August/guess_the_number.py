'''
Created on 11-Aug-2015

@author:  Venkatesh

Guess the Number

'''


import fractions


def min_val(inp):
    y_pos, n_pos = [], []
    for idx, ch in enumerate(inp):
        if ch == 'Y':
            y_pos.append(idx+1)
        else:
            n_pos.append(idx+1)
    lcm = 1
    for ele in y_pos:
        lcm = lcm * ele / fractions.gcd(lcm, ele)
    # verify the operation now
    # print lcm
    for cur in n_pos:
        if lcm % cur == 0:
            return -1
    return lcm


def main():
    while True:
        inp = raw_input()
        if inp == "*":
            return
        else:
            print min_val(inp)


if __name__ == '__main__':
    main()
