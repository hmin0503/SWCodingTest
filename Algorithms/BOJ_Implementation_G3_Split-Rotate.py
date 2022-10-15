#------------------------
# #Implementation #Simulation #Split #Rotate #Efficiency #pypy3 
# https://www.acmicpc.net/problem/20058
#------------------------

# 단계 L을 결정
# 부분 격자 시계방향 90도 회전 -> 격자 나누기 / 90도 회전
# 각 얼음칸을 기준으로 주변에 얼음이 3개 이상 없으면 1개씩 줄어듬 -> melting() (얼음이 없을땐 실행 안함.)

# 얼음의 총합
# 가장 큰 얼음 덩어리 -> dfs

def splitNrotate(l, iceberg):
    split = []
    for r in range(0, 2**N, 2**l):
        for c in range(0, 2**N, 2**l):
            # Split
            tmp = [iceberg[nr][c:(c+2**l)] for nr in range(r, r+2**l)]
            # Rotate
            tmp = list(map(list, zip(*reversed(tmp))))
            split.append(tmp)
    # for row in split: print(row)
    # print()
    # Merge
    merge = []
    for r in range(0, 2**(N-l)):
        # print(split[r*(2**(N-l)):(r+1)*(2**(N-l))])
        for row in zip(*split[r*(2**(N-l)):(r+1)*(2**(N-l))]):
            merge.append(list(sum(row, [])))

    # print(f"Merge, size: {l}")
    # for a, b in zip(iceberg, merge):print(*a," ",*b)
    return merge

def melting(iceberg):
    tmp = deepcopy(iceberg)
    for r in range(2**N):
        for c in range(2**N):
            if iceberg[r][c] > 0:
                around = 0
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < 2**N and 0 <= nc < 2 ** N:
                        if iceberg[nr][nc] > 0:
                            around += 1
                    else:
                        continue
                if around < 3:
                    tmp[r][c] -= 1
    return tmp

def bfs(r,c):
    size = 1
    queue = deque([(r,c)])
    visited[r][c] = 1
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 2**N and 0 <= nc < 2**N :
                if iceberg[nr][nc] > 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    queue.append((nr,nc))
                    size += 1
    return size

from collections import deque
from copy import deepcopy
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, Q = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(2**N)]
level = list(map(int, input().split()))
for l in level:
    if l != 0:
        iceberg = splitNrotate(l, iceberg)
    iceberg = melting(iceberg)    

# 얼음 갯수 세기.
total = 0
for r in range(2**N):
    for c in range(2**N):
        total += iceberg[r][c]
print(total)

# 가장 큰 얼음 덩어리 찾기.
visited = [[0]* (2**N) for _ in range(2**N)]
maximum = 0
for r in range(2**N):
    for c in range(2**N):
        if iceberg[r][c] > 0 and visited[r][c] == 0:
            size = bfs(r,c)
            if maximum < size:
                maximum = size
print(maximum)
