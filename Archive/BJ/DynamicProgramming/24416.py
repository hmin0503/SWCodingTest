#------------------------
# #DP #Bronze1 #pypy3
# https://www.acmicpc.net/problem/24416
#------------------------

def fibo_re(n):
    global cnt_re
    if n == 1 or n == 2:
        return 1
    else:
        cnt_re += 1
        return fibo_re(n-1)+fibo_re(n-2)
    
def fibo_dp(n):
    global cnt_dp
    memo[1] = 1
    memo[2] = 1
    for i in range(3, n):
        cnt_dp += 1
        memo[i] = memo[i-1]+memo[i-2]
    

if __name__ == '__main__':
    n = int(input())
    
    memo = [0] * (n+1)

    cnt_re = 1
    cnt_dp = 1
    
    fibo_re(n)
    fibo_dp(n)
    print(cnt_re, cnt_dp)
    
