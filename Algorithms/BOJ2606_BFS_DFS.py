#------------------------
# #BFS #DFS #Graph #Traversal #Queue #Recursion
# https://www.acmicpc.net/problem/24444
#------------------------
from collections import deque
import sys

def bfs(s):
    cnt = 0
    visited = [False] * (N+1)
    visited[s] = True
    queue = deque([s])
    while queue:
        q = queue.popleft()
        for n in graph[q]:
            if not visited[n]:
                visited[n] = True
                queue.append(n)
                cnt += 1
    print(cnt)

def dfs(s, visited):
    global cnt
    visited[s] = True
    for n in graph[s]:
        if not visited[n]:
            cnt += 1
            dfs(n, visited)
if __name__ == '__main__':
    N = int(input()) # <= 100
    M = int(input())
    graph = {i:[] for i in range(1, N+1)}
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    # BFS
    bfs(1)    
    
    # DFS
    cnt = 0
    visited = [0]*(N+1)
    dfs(1, visited)
    print(cnt)


