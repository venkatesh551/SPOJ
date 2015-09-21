'''
Created on 21-Sep-2015

@author: Venkatesh

SAMER08F - Feynman
'''


def read_int():
    return int(raw_input())


def no_of_squares(n):
    """
If n = 1, there is one 1-by-1 square.

If n = 2, there is one 2-by-2 square and four 1-by-1 squares.

If n = 3, there is one 3-by-3 square, four 2-by-2 squares
and nine 1-by-1 squares.

If we continued the above sequence for an arbitrary n,
then we would have one n-by-n square,
four (n - 1)-by-(n - 1) squares,
nine (n - 2)-by-(n - 2) squares, ... , and n**2 1-by-1 squares.
"""
    return n * (n + 1) * (2 * n + 1) / 6


def main():
    while True:
        n = read_int()
        if n == 0:
            return
        print no_of_squares(n)


if __name__ == '__main__':
    main()
