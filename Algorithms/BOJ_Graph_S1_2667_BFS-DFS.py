#------------------------
# #BFS #Graph #Traversal #Queue #Implementation
# https://www.acmicpc.net/problem/2667
#------------------------
from collections import deque
import sys
sys.setrecursionlimit(10**9)
def dfs(maps, r, c):
    global cnt
    if c <= -1 or c >= len(maps) or r <= -1 or r >= len(maps):
        return False
    
    if maps[r][c] == 1:
        cnt += 1
        maps[r][c] = 0
        dfs(maps, r-1, c) # 상
        dfs(maps, r, c-1) # 좌
        dfs(maps, r+1, c) # 하
        dfs(maps, r, c+1) # 우
        return True
    return False
    
def bfs(r,c):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    cnt = 1
    queue = deque([(r,c)])
    visited[r][c] = True

    while queue:
        sr, sc = queue.popleft()
        for i in range(4):
            nr = sr + dr[i]
            nc = sc + dc[i]
            if 0<=nr<N and 0<=nc<N and town[nr][nc] == '1':
                if not visited[nr][nc] :
                    cnt += 1
                    visited[nr][nc] = True
                    queue.append((nr,nc))
    return cnt

if __name__ == '__main__':
    N = int(input())
    town = [list(input()) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    cnts = []
    for r in range(N):
        for c in range(N):
            if town[r][c] == '1' and not visited[r][c]:
                cnts.append(bfs(r,c))
    cnts = sorted(cnts)

    print(len(cnts))
    for c in cnts: print(c)