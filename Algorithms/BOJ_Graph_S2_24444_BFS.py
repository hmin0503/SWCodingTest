#------------------------
# #BFS #Graph #Traversal #Queue
# https://www.acmicpc.net/problem/24444
#------------------------
from collections import deque
import sys

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

    # BFS
    cnt = 1
    visited[R] = cnt
    queue = deque([R])
    while queue:
        q = queue.popleft()
        for n in graph[q]:
            if visited[n] == 0:
                cnt += 1
                visited[n] = cnt
                queue.append(n)
    
    for i in visited[1:]:
        print(i)