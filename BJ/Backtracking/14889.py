#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #BackTracking #DFS #Silver2
# https://www.acmicpc.net/problem/14889
#------------------------

def dfs(st):
    global minimum
    if len(lst) == N//2:
        results1, results2 = 0, 0
        for i in range(N):
            for j in range(N):
                if i not in lst and j not in lst:
                    results2 += tabs[i][j]
                elif i in lst and j in lst:
                    results1 += tabs[i][j]
        minimum = min(abs(results1-results2), minimum)
        return
    
    for num in range(st, N):
        if num not in lst:
            lst.append(num)
            dfs(num+1)
            lst.pop()
            
if __name__ == '__main__':
    minimum = 1e9
    
    N = int(input())
    tabs = [list(map(int, input().split())) for _ in range(N)]
    
    lst = []
    dfs(0)
    print(minimum)
