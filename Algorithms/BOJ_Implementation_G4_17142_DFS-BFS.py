#------------------------
# #Implementation #Simulation #BruteForce #DFS #BFS
# https://www.acmicpc.net/problem/17142
#------------------------
'''
TEST CASE 1
5 1
2 2 2 1 1
2 1 1 1 1
2 1 1 1 1
2 1 1 1 1
2 2 2 1 1

AWS 0
'''

'''
TEST CASE 2
5 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
2 0 0 2 0
1 1 1 1 1

AWS 2
'''

'''
TEST CASE 3
9 1
0 2 2 2 2 2 2 2 0
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
4

AWS 4
'''       
# def dfs(maps, A, M):
#     global minimum
#     # M개를 골랐다면,
#     if len(A) == M:
#         h, visits = bfs(A, maps)
#         # 모든 칸을 다 방문 했는가?
#         if visits == N*N-walls:
#             if minimum > h:
#                 minimum = h
#         return
    
#     for idx in range(len(V)):
#         if V[idx] not in A:
#             A.append(V[idx])
#             dfs(maps, A, M)
#             A.pop()

def check(maps):
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 0:
                return False
    return True

def bfs(A, maps):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    visited = [[0] * N for _ in range(N)]
    queue = deque(A)
    for r, c, _ in A:
        visited[r][c] = 1
    visits = len(A)
    last = 0
    while queue:
        r, c, t = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # N x N 범위 이내인가.
            if 0 <= nr < len(maps) and 0 <= nc < len(maps):
                # 바이러스가 퍼지지 않은 곳. AND 벽이 아닌 곳.
                if visited[nr][nc] == 0 and maps[nr][nc] != 1:
                    visited[nr][nc] = 1
                    queue.append((nr, nc, t + 1))
                    visits += 1
                    if maps[nr][nc] == 0:
                        maps[nr][nc] = 2
                        last = t + 1
    if check(maps):
        return last
    else:
        return -1

from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

V = []
walls = 0
for r in range(N):
    for c in range(N):
        if maps[r][c] == 2:
            V.append((r,c,0))
        if maps[r][c] == 1:
            walls += 1
virus_comb = combinations(V, M)

minimum = 1e9
for virus in virus_comb:
    newMaps = deepcopy(maps)
    time = bfs(virus, newMaps)
    if minimum > time and time > -1:
        minimum = time

if minimum != 1e9:
    print(minimum)
else:
    print(-1)