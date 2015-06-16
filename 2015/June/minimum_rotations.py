'''
Created on 16-Jun-2015

@author: Venkatesh

MINMOVE - Minimum Rotations

'''


def get_min_rotation(inp_str):
    ans, smallest = 0, inp_str
    i,  n = 0, len(inp_str)
    while i < n:
        i += 1
        rotated_str = inp_str[i:n] + inp_str[0:i]
        if rotated_str < smallest:
            ans, smallest = i, rotated_str
    return ans


def main():
    inp_str = raw_input()
    print get_min_rotation(inp_str)

if __name__ == '__main__':
    main()
