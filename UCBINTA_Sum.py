def main():
    n = int(raw_input())
    A = [0] * n
    for i in xrange(n):
        A[i] = map(int, raw_input().split())
    if n == 2:
        print A[0][1]/2, A[0][1]/2
        return
    total = 0
    for i in xrange(n):
        for j in xrange(i+1, n, 1):
           total += A[i][j]
    row0 = sum(A[0])
    e1 = (row0 - total/(n-1)) / (n-2)
    print e1,
    A[0].pop(0)
    for ele in A[0]:
          print ele - e1,

if __name__ == '__main__':
    main()
