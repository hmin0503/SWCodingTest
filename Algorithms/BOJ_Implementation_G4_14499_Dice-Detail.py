#------------------------
# #Implementation #Simulation
# https://www.acmicpc.net/problem/14499
#------------------------
def rollDice(v, h):
    if d == 1: # 동쪽
        nv = [v[0], h[0], v[2], h[-1]]
        nh = [v[-1], h[0], h[1]]
    elif d == 2: # 서쪽
        nv = [v[0], h[-1], v[2], h[0]]
        nh = [h[1], h[-1], v[-1]]
    elif d == 3: # 남쪽
        nv = v[1:] + [v[0]]
        nh = [h[0], v[2], h[-1]]
    elif d == 4: # 북쪽
        nv = [v[-1]] + v[:-1]
        nh = [h[0], v[0], h[-1]]
    return nv, nh

if __name__ == "__main__":
    N, M, r, c, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    commands = list(map(int,input().split()))
    
    # v = [2,1,5,6]
    # h = [4,1,3]
    v = [0, 0, 0, 0]
    h = [0, 0, 0]

    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    for d in commands:
        nr = r + dr[d-1]
        nc = c + dc[d-1]
        if 0 <= nr < N and 0 <= nc < M:
            r, c = nr, nc
            v, h = rollDice(v, h)
            if maps[r][c] == 0:
                maps[r][c] = v[-1]
            else:
                v[-1] = maps[r][c]
                maps[r][c] = 0
            print(v[1])
        else:
            continue



