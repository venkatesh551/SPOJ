'''
Created on 28-Sep-2015

@author: Venkatesh
'''


def no_of_diff_decodings(code):
    prev = 0
    n = len(code)
    dp = [0] * (n+1)
    dp[0] = 1
    for idx, ch in enumerate(code):
        i = idx + 1
        cur = ord(ch) - ord('0')
        val = prev * 10 + cur
        if cur == 0:
            dp[i] = dp[i-2]
        elif val > 9 and val < 27:
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]
        prev = cur
    return dp[n]


def main():
    while True:
        code = raw_input()
        if code == "0":
            return
        print no_of_diff_decodings(code)

if __name__ == '__main__':
    main()
