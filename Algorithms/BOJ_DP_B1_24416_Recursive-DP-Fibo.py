#------------------------
# #DP #Fibonacci #pypy3
# https://www.acmicpc.net/problem/24416
#------------------------

def fiboRe(n):
    global cntRe
    if n == 1 or n == 2:
        cntRe += 1
        return 1
    return fiboRe(n-1) + fiboRe(n-2)

def fiboDP(n):
    global cntDP
    dp = [0] * (n+1)
    dp[1] = dp[2] = 1
    if n > 2:
        for i in range(3, n+1):
            cntDP += 1
            dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


if __name__ == '__main__':
    n = int(input())
    cntRe = cntDP = 0
    fiboRe(n)
    fiboDP(n)
    print(cntRe, cntDP)