#------------------------
# #Implementation #Simulation #Queue #Efficiency #pypy3
# https://www.acmicpc.net/problem/21610
#------------------------

def moveCloud(C, d, s):
    dr = [0, -1, -1, -1, 0, 1, 1, 1]
    dc = [-1, -1, 0, 1, 1, 1, 0, -1]
    for _ in range(len(C)):
        r, c = C.popleft()
        nr , nc = (r + dr[d-1]*s)%N, (c + dc[d-1]*s)%N
        C.append((nr,nc))
    return C

def rain(A, C):
    for r, c in C:
        A[r][c] += 1
    return A

def copyWater(A, C):
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, 1, -1]
    for r, c in C:
        total = 0
        for i in range(4):
            nr , nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and A[nr][nc] > 0:
                total += 1
        A[r][c] += total
    return A

def generateCloud(A, C):
    newC = deque([])
    for r in range(N):
        for c in range(N):
            if A[r][c] >= 2 and (r,c) not in C:
                newC.append((r,c))
                A[r][c] -= 2
    return newC

from collections import deque

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    
    C = deque([(N-1,0), (N-1, 1), (N-2, 0), (N-2, 1)])
    for _ in range(M):
        d, s = map(int, input().split())
        C = moveCloud(C, d, s)
        A = rain(A, C)
        A = copyWater(A, C)
        C = generateCloud(A, C)

    print(sum([sum(row) for row in A]))

