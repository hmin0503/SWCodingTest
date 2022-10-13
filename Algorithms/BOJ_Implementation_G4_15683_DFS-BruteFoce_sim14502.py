#------------------------
# #Implementation #Simulation #BruteForce #DFS #pypy3 #Efficiency?
# https://www.acmicpc.net/problem/15683
#------------------------
from copy import deepcopy
import sys
sys.setrecursionlimit(1000000000)
def dfs(d, t, r, c, offices):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    if 0 > r or r >= len(offices) or 0 > c or c >= len(offices[0]):
        return 
    if offices[r][c] != 6:
        if offices[r][c] == 0:
            offices[r][c] = "#"
        if t == 1:
            nr = r + dr[d]
            nc = r + dc[d]
            dfs(d, t, nr, nc, offices)
        elif t == 2:
            dfs(d, t, r + dr[d], r + dc[d], offices)
            dfs(d, t, r - dr[d], r - dc[d], offices)
        elif t == 3:
            dfs(d, t, r + dr[d], r + dc[d], offices)
            dfs(d, t, r + dr[(d+1)%4], r + dc[(d+1)%4], offices)
        elif t == 4:
            dfs(d, t, r + dr[d], r + dc[d], offices)
            dfs(d, t, r + dr[(d+1)%4], r + dc[(d+1)%4], offices)
            dfs(d, t, r + dr[(d+2)%4], r + dc[(d+2)%4], offices)
        elif t == 5:
            dfs(d, t, r + dr[d], r + dc[d], offices)
            dfs(d, t, r + dr[(d+1)%4], r + dc[(d+1)%4], offices)
            dfs(d, t, r + dr[(d+2)%4], r + dc[(d+2)%4], offices)
            dfs(d, t, r + dr[(d+3)%4], r + dc[(d+3)%4], offices)
    return offices
    
def combinations(cctv, direction):
    print(direction)
    global minimum
    if len(direction) == len(cctv):
        newOffices = deepcopy(offices)
        for d, (t, r, c) in zip(direction, cctv):
            newOffices = dfs(d, t, r, c, newOffices)
        total = 0
        for r in range(len(offices)):
            for c in range(len(offices[0])):
                if offices[r][c] == 0:
                    total += 1
        if minimum > total:
            minimum = total
        return
    for i in range(len(cctv)):
        for d in range(4):
            direction.append(d)
            combinations(cctv, direction)
            direction.pop()

if __name__ == '__main__':
    N, M = map(int, input().split())
    offices = [list(map(int, input().split())) for _ in range(N)]
    cctv = []
    walls = 0
    for r in range(N):
        for c in range(M):
            if 0 < offices[r][c] < 6:
                cctv.append((offices[r][c], r, c))
            elif offices[r][c] == 6:
                walls += 1

    minimum = 1e9
    combinations(cctv, [])
    print(N*M)
    print(N*M - len(cctv) - walls - minimum)