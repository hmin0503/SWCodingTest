#------------------------
# #Implementation #Simulation #Spiral
# https://www.acmicpc.net/problem/20057
#------------------------

# 토네이도는 나선형으로 이동
# 이동하는 칸 모래는 주변으로 흩날림
import math

def moveSand(r, c, d): # r,c 는 이동 후 좌표값
    outSand = 0
    totalSand = maps[r][c]
    # # ← ↙ ↓ ↘ → ↑ ↗ ↑ ↖ ←
    # ddr = [0, 1, 1, 1, 0, -1, -1, -1]
    # ddc = [-1, -1, 0, 1, 1, 1, 0, -1]

    # 서남동북(반시계방향)
    # 서쪽기준으로 시계방향: 북쪽, 반시계방향: 남쪽
    # 남쪽기준으로 시계방향: 서쪽, 반시계방향: 동쪽

    # 90도 시계방향 한번 전진.
    nr = r + dr[(d-1)%4]
    nc = c + dc[(d-1)%4]
    sand = math.trunc(maps[r][c]*0.07)
    totalSand -= sand
    if 0 <= nr < N and 0 <= nc < N:
        maps[nr][nc] += sand
    else:
        outSand += sand

    # 90도 시계방향 두번 전진.
    nr = r + dr[(d-1)%4]*2
    nc = c + dc[(d-1)%4]*2
    sand = math.trunc(maps[r][c]*0.02)
    totalSand -= sand
    if 0 <= nr < N and 0 <= nc < N:
        maps[nr][nc] += sand
    else:
        outSand += sand

    # 90도 반시계방향 한번 전진.
    nr = r + dr[(d+1)%4]
    nc = c + dc[(d+1)%4]
    sand = math.trunc(maps[r][c]*0.07)
    totalSand -= sand
    if 0 <= nr < N and 0 <= nc < N:
        maps[nr][nc] += sand
    else:
        outSand += sand

    # 90도 반시계방향 두번 전진.
    nr = r + dr[(d+1)%4]*2
    nc = c + dc[(d+1)%4]*2
    sand = math.trunc(maps[r][c]*0.02)
    totalSand -= sand
    if 0 <= nr < N and 0 <= nc < N:
        maps[nr][nc] += sand
    else:
        outSand += sand

    # 45도 시계방향 전진.
    nr = r+dr[d]+dr[(d-1)%4]
    nc = c+dc[d]+dc[(d-1)%4]
    sand = math.trunc(maps[r][c]*0.1)
    totalSand -= sand
    if 0 <= nr < N and 0 <= nc < N:
        maps[nr][nc] += sand
    else:
        outSand += sand
    
    # 45도 반시계방향 전진.
    nr = r+dr[d]+dr[(d+1)%4]
    nc = c+dc[d]+dc[(d+1)%4]
    sand = math.trunc(maps[r][c]*0.1)
    totalSand -= sand
    if 0 <= nr < N and 0 <= nc < N:
        maps[nr][nc] += sand
    else:
        outSand += sand

    # 135도 시계방향 전진.
    nr = r+dr[(d-1)%4]+dr[(d-2)%4]
    nc = c+dc[(d-1)%4]+dc[(d-2)%4]
    sand = math.trunc(maps[r][c] * 0.01)
    totalSand -= sand
    if 0 <= nr < N and 0 <= nc < N:
        maps[nr][nc] += sand
    else:
        outSand += sand
    
    # 135도 반시계방향 전진.
    nr = r+dr[(d+1)%4]+dr[(d+2)%4]
    nc = c+dc[(d+1)%4]+dc[(d+2)%4]
    sand = math.trunc(maps[r][c] * 0.01)
    totalSand -= sand
    if 0 <= nr < N and 0 <= nc < N:
        maps[nr][nc] += sand
    else:
        outSand += sand

    # 해당 방향 두번 전진.
    nr = r + dr[d]*2
    nc = c + dc[d]*2
    sand = math.trunc(maps[r][c]*0.05)
    totalSand -= sand
    if 0 <= nr < N and 0 <= nc < N:
        maps[nr][nc] += sand
    else:
        outSand += sand
        
    # 해당 방향 한번 전진.
    nr = r + dr[d]
    nc = c + dc[d]
    if 0 <= nr < N and 0 <= nc < N:
        maps[nr][nc] += totalSand
    else:
        outSand += totalSand

    # 해당 위치 모래 삭제.
    maps[r][c] = 0
    return outSand

answers = 0

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

# 좌하우상(반시계방향)
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

sr, sc = N // 2, N // 2
r, c = sr, sc
d = 0 # 방향
cnt = 0 # 방향 전환 횟수 -> 방향 2번 전환 후 전진 횟수 1 증가.
dist = 1 # 해당 방향으로 전진 횟수

while (r,c) != (0,0):
    cnt += 1
    for _ in range(dist):
        nr, nc = r + dr[d], c + dc[d]
        if (nr, nc) == (0, -1):
            break
        r, c = nr, nc
        answers += moveSand(r, c, d)
        # print(r, c, d, answers)
        # print("Sand")
        # for row in maps: print(*row)
        # print()
    if cnt == 2:
        dist += 1
        cnt = 0
    d = (d+1)%4
print(answers)

