'''
Created on 20-Sep-2015

@author: venkat
'''

import sys


def main():
    for line in sys.stdin:
        n = long(line)
        print 2 * (n-1) if n > 1 else "1"

if __name__ == '__main__':
    main()
