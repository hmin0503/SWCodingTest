#------------------------
# #Implementation #Simulation #Efficiency #DFS #BFS
# https://www.acmicpc.net/problem/23290
#------------------------


def moveFish(fish):
    dr = [0, -1, -1, -1, 0, 1, 1, 1]
    dc = [-1, -1, 0, 1, 1, 1, 0, -1]
    fish = deque(fish)
    for i in range(len(fish)):
        r, c, d = fish.popleft()
        nd = d
        while True:
            nr = r + dr[nd]
            nc = c + dc[nd]
            # 이동 후 범위 안에 있는가? 상어가 없는가? 또는 물고기 냄새가 없는가?
            if 0 <= nr < 4 and 0 <= nc < 4 and maps[nr][nc] == 0:
                fishMaps[r][c] -= 1
                fishMaps[nr][nc] += 1
                fish.append((nr,nc,d))
            else:
                nd = (d-1)%8
            if d == nd:
                break
    return fish

def moveShark(r, c):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 상어 방향 찾기.
    answers = -1e9
    for i in range(4):
        kill = 0
        nr = r + dr[i]*3
        nc = c + dc[i]*3
        #  이동 가능 한가?
        if 0 <= nr < 4 and 0 <= nc < 4:
            for j in range(3):
                nr = r + dr[j]
                nc = c + dc[j]
                kill += fishMaps[nr][nc]
        if answers < kill :
            answer = kill
            d = i
    
    # 상어 이동하기
    for i in range(3):
        nr = r + dr[d]
        nc = r + dc[d]
        fishMaps[nr][nc] = 0
        maps[nr][nc] = 2




from copy import deepcopy
from collections import deque

if __name__ == '__main__':
    M, S = map(int, input().split())
    # 상어:1, 물고기냄새:2
    maps = [[0]*4 for _ in range(4)]
    fishMaps = [[0]*4 for _ in range(4)]
    fish = []
    for _ in range(M):
        r, c, d = map(int, input().split())
        d -= 1
        fish.append((r,c,d))
        fishMaps[r][c] += 1
    sr, sc = map(int, input().split())
    maps[sr][sc] = 1

    for _ in range(S):
        copyFish = deepcopy(fish)
        fish = moveFish(fish)
        