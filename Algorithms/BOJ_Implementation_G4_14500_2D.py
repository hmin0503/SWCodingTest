#------------------------
# #Implementation #Simulation #BruteForce #pypy3
# https://www.acmicpc.net/problem/14500
#------------------------
def rotate(d):
    return
def flip():
    return
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def b1Score(r, c):
    
    return r, c
def b2Score(r, c):

def b3Score(r, c):

def b4Score(r, c):

def b5Score(r, c):

def check(b, r, c):
    total = 0
    # 북동남서
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        for d in range(2):
            if b == 0:
                if i == 0:
                    nr = r + dr[i]*3
                    nc = c + dc[i]*3
                    if 0 <= nr < N and 0 <= nc < N:
                        for t in range(r, nr+1):
                            total += maps[t][nc]
                



if __name__ == '__main__':
    N, M = map(int, input())
    maps = [list(map(int, input().split())) for _ in range(M)]
    visited = [[0] * N for _ in range(N)]
    for b in range(5):
        for r in range(N):
            for c in range(N):
                calculate