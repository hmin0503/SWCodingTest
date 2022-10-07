#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #BackTracking #DFS #Silver1 
# https://www.acmicpc.net/problem/14888
#------------------------

def dfs(n, total, add, sub, mul, div):
    global maximum, minimum
    if n == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    
    if add:
        dfs(n+1, total + nums[n], add -1, sub, mul, div)
    if sub:
        dfs(n+1, total - nums[n], add, sub -1, mul, div)
    if mul:
        dfs(n+1, total * nums[n], add, sub, mul - 1, div)
    if div:
        dfs(n+1, int(total / nums[n]), add, sub, mul, div - 1)    
    
    
if __name__ == '__main__':
    maximum = -1e9
    minimum = 1e9
    
    N = int(input())
    nums = list(map(int, input().split()))
    ops = list(map(int, input().split()))
    dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])
    
    print(maximum)
    print(minimum)
    

