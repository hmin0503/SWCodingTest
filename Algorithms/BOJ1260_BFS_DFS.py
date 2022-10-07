#------------------------
# #BFS #DFS #Graph #Traversal #Queue #Recursion
# https://www.acmicpc.net/problem/1260
#------------------------
from collections import deque
import sys

def bfs(s):
    visited = [False] * (N+1)
    visited[s] = True
    print(s, end = " ")
    queue = deque([s])
    while queue:
        q = queue.popleft()
        graph[q].sort()
        for n in graph[q]:
            if not visited[n]:
                visited[n] = True
                print(n, end = " ")
                queue.append(n)

def dfs(s, visited):
    visited[s] = True
    print(s, end = " ")
    graph[s].sort()
    for n in graph[s]:
        if not visited[n]:
            dfs(n, visited)

if __name__ == '__main__':
    N, M, R = map(int, input().split()) # <= 100
    graph = {i:[] for i in range(1, N+1)}
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # DFS
    visited = [0]*(N+1)
    dfs(R, visited)
    print()
    # BFS
    bfs(R)    


