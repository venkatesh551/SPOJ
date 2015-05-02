def solve():
    t = int(raw_input())
    P = 1298074214633706835075030044377087
    for _ in xrange(t):
        n = int(raw_input())
        print pow(2, n+1, P)-1

if __name__ == '__main__':
    solve()
