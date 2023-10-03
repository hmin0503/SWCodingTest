import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # 재귀 함수 빈도 10000 으로 증가

def melting(grid):
    grid_ = [[0] * M for _ in range(N)]
    for r in range(1, N):
        for c in range(1, M):
            if grid[r][c] > 0:
                water = 0
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if (0 <= nr < N and 0 <= nc < M) and grid[nr][nc] == 0:
                        water += 1
                grid_[r][c] = max(grid[r][c] - water, 0)
    return grid_

def dfs(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if (0 <= nr < N and 0 <= nc < M) and  visited[nr][nc] == 0 and grid[nr][nc] != 0:
            visited[nr][nc] = 1
            dfs(nr, nc)

N, M = map(int, input().split())
grid = [list(map(int, input().strip().split())) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 1
time = 0

# (0) 모든 빙하가 녹을 때 까지 진행
while sum([sum(g) for g in grid]) > 0: 
    # (1) 빙하가 녹는다
    grid = melting(grid)
    time += 1

    # (2) 빙산 덩어리 개수 구하기
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for r in range(1, N):
        for c in range(1, M):
            if grid[r][c] != 0 and visited[r][c] == 0:
                cnt += 1
                visited[r][c] = 1
                dfs(r, c)
    # (3) 빙산 덩어리가 두 개 이상이면 stop!
    if cnt > 1:
        print(time)
        break
# (4) **모든 빙하가 다 녹을 때 까지 두 개로 나뉘어 지지 않으면 "0" 출력!
else:
    print(0)