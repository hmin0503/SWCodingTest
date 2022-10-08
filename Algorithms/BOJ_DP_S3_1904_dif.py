#------------------------
# #DP 
# https://www.acmicpc.net/problem/1904
#------------------------

def tile(n):
    for i in range(3, n+1):
        dp[i] = (dp[i-2] + dp[i-1])%15746
    return dp[n]
if __name__ == '__main__':
    N = int(input())
    dp = [0] * (N+1)
    dp[1] = 1
    if N > 1 :
        dp[2] = 2
        print(tile(N))
    else:
        print(dp[1])