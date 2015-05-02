__author__ = 'Venkatesh'

def main():
    n = long(raw_input())
    while n > 3:
        n >>= 1
    print ('TIE' if n == 3 else "TAK")

if __name__ == '__main__':
    main()
