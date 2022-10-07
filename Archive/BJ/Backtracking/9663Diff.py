#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #BackTracking #DFS #Gold4 #pypy3 #TooSlow
# https://www.acmicpc.net/problem/9663
#------------------------


def dfs(n):
    if n == N:
        global cnt
        cnt += 1
        return
    
    for i in range(N):
        visited[n] = i
        if check_diag(n):
            dfs(n+1)
            
def check_diag(q):
    for i in range(q):
        if (abs(visited[q] - visited[i]) == (q-i)) or (visited[q] == visited[i]):
            return False
    return True
    

if __name__ == '__main__':
    N = int(input())
    visited = [-1]*N
    cnt = 0
    dfs(0)
    print(cnt)
    