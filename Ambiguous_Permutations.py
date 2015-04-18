def solve():
    while True:
        n = int(raw_input())
        if n == 0:
            return
        A = map(int, raw_input().split())
        is_amb = True
        for i in range(n):
            if i+1 != A[A[i]-1]:
                is_amb = False
                break
        print ( 'ambiguous' if is_amb else 'not ambiguous')
if  __name__ == '__main__':
    solve()
