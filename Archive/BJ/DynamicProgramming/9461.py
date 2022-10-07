#------------------------
# #DP #Silver3
# https://www.acmicpc.net/problem/9461
# 점화식 구하기!
#------------------------

def main(N):
    if N in memo:
        return memo[N]
    
    for n in range(1, N-2):
        memo[n+3] = memo[n] + memo[n+1]        
        
    return memo[N]
    
if __name__ == '__main__':
    T = int(input())
    memo = {}
    memo[1] = 1
    memo[2] = 1
    memo[3] = 1
    for _ in range(T):
        N = int(input())
        print(main(N))
    