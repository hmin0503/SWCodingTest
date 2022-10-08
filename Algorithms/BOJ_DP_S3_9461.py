#------------------------
# #DP #Math
# https://www.acmicpc.net/problem/9461
#------------------------

def triangle(n):
    for i in range(1, n+1):
        if i < 4:
            dp[i] = 1
        elif i == 4 or i == 5:
            dp[i] = 2
        else:
            dp[i] = dp[i-1] + dp[i-5]
    return dp[n]
if __name__ == '__main__':
    T = int(input())
    dp = [0] * (101)
    for _ in range(T):
        N = int(input())
        print(triangle(N))

