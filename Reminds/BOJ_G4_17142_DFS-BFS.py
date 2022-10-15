#-----------------------------------------------
# 연구소3 G4
# https://www.acmicpc.net/problem/17142
#-----------------------------------------------
# 모든 바이러스 비활성 상태
# 활성 바이러스 주위로 빈 공간에 바이러스 복제, 
    # 비활성 바이러스는 활성됨.
# 모든 바이러스 활성하는데 걸리는 시간?
# 모든 바이러스 활성 불가능시 -1
# 비활성 바이러스 활성하는 것은 last time에 포함 안됨.
#-----------------------------------------------
def check(newLabs):
    for r in range(N):
        for c in range(N):
            if newLabs[r][c] == 0:
                return False
    return True

def bfs(newLabs, selection):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0 ,-1]
    visited = [[0] * N for _ in range(N)]
    queue = deque([])
    for s in selection:
        r, c = viruses[s]
        queue.append((r, c, 0))
        visited[r][c] = 1 # 큐는 기존 위치 방문처리 무조건 필수.
    last_time = 0
    while queue:
        r, c, t = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 0 and newLabs[nr][nc] != 1:
                    visited[nr][nc] = 1
                    queue.append((nr,nc,t+1))
                    if newLabs[nr][nc] == 0:
                        newLabs[nr][nc] = 2
                        last_time = t + 1
    if check(newLabs):
        return last_time
    else:
        return 1e9
                    
def dfs(selection, st):
    global minimum
    if len(selection) == M:
        newLabs = deepcopy(labs)
        minimum = min(minimum, bfs(newLabs, selection))
        return 
    for i in range(st, len(viruses)):
        if i not in selection:
            selection.append(i)
            dfs(selection, i + 1)
            selection.pop()

from collections import deque
from copy import deepcopy
minimum = 1e9
N, M = map(int, input().split())
labs = [list(map(int, input().split())) for _ in range(N)]
viruses = []
for r in range(N):
    for c in range(N):
        if labs[r][c] == 2:
            viruses.append((r,c))
dfs([], 0)
if minimum == 1e9:
    print(-1)
else:
    print(minimum)


