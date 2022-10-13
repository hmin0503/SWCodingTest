#------------------------
# #Implementation #Simulation #BruteForce #BFS #pypy3 #Efficiency?
# https://www.acmicpc.net/problem/14502
#------------------------
from collections import deque
from copy import deepcopy
def spread(maps, r, c):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    total = 0
    queue = deque([(r, c)])
    while queue:
        sr, sc = queue.popleft()
        for i in range(4):
            nr = sr + dr[i]
            nc = sc + dc[i]
            if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]):
                if maps[nr][nc] == 0:
                    total += 1
                    maps[nr][nc] = 3
                    queue.append((nr, nc))
    return maps

def dfs(V, w):
    global maximum
    if w == 3:
        # print("After building")
        # for row in maps: print(*row)
        total = 0
        newMaps = deepcopy(maps)
        for r, c in V:
            newMaps = spread(newMaps, r, c)
        # print("After spreading")
        # for row in newMaps: print(*row)
        
        for r in range(len(maps)):
            for c in range(len(maps[0])):
                if newMaps[r][c] == 0:
                    total += 1
        if maximum < total:
            maximum = total
        return

    for r in range(N):
        for c in range(M):
            if maps[r][c] == 0:
                maps[r][c] = 1
                dfs(V, w+1)
                maps[r][c] = 0


if __name__ == '__main__':
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    V = []
    for r in range(N):
        for c in range(M):
            if maps[r][c] == 2:
                V.append((r,c))
    
    maximum = -1e9
    dfs(V, 0)
    print(maximum)