#------------------------
# #DFS #Graph #Traversal #Recursive
# https://www.acmicpc.net/problem/24479
#------------------------
import sys
sys.setrecursionlimit(10**9)

def dfs(s):
    global cnt
    visited[s] = cnt
    for n in graph[s]:
        if visited[n] == 0 :
            cnt += 1
            dfs(n)

if __name__ == '__main__':
    N, M, R = map(int,input().split())
    graph = {i:[] for i in range(1, N+1)}
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0] * (N+1)

    #오름차순 방문 -> 내림차순 정렬
    graph = {k:sorted(v, reverse = False) for k,v in graph.items()}
    cnt = 1
    dfs(R)

    for i in visited[1:]:
        print(i)