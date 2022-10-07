#------------------------
# 구슬 탈출 2
# https://www.acmicpc.net/problem/13460
#------------------------
from collections import deque

def marbleEscape2(ry, rx, by, bx):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    q = deque()
    q.append((rx, ry, bx, by))
    visited = set()
    visited.append(q[0])
    cnt = 0

    while q:
        if cnt > 10:
            return -1   
        rx, ry, bx, by = q.popleft()
        if maps[ry][rx] == "O":
            return cnt
        for i in range(4):
            nry, nrx = ry + dy[i], rx + dx[i]
            while True:
                if maps[nry][nrx] == "#":
                    nry, nrx = ry, rx
                    break
                if maps[nry][nrx] == "O":
                    break
            
            nbx, nby = by + dy[i] , bx + dx[i]
            while True:
                if maps[nby][nbx] == "#":
                    nby, nbx = by, bx
                    break
                if maps[nby][nbx] == "O":
                    break 

            if maps[nby][nbx] == "#":
                 continue
            
            if nry == nby and nrx == nbx:



if __name__ == '__main__':
    n,m = map(int, input().split())
    maps = [list(input()) for _ in range(n)]
    print(maps)
    for y in range(n):
        for x in range(m):
            if maps[y][x] == "R":
                ry, rx = y, x
            elif maps[y][x] == "B":
                by, bx = y, x

    cnt = 0
    print(marbleEscape2(ry, rx, by, bx))
