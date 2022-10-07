#------------------------
# #DP #Silver3
# https://www.acmicpc.net/problem/1904
# 점화식이 이해가 안간다?
#------------------------

def solution(n):
    memo[2] = 2
    
    for i in range(3, n+1):
        memo[i] = (memo[i-2] + memo[i-1])%15746
            
    
if __name__ == '__main__':
    n = int(input())
    memo = [0] * (n+1)
    memo[1] = 1
    if n > 1:
        solution(n)
    print(memo[n])
    
    