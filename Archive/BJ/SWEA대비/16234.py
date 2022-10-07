#------------------------
# 인구 이동
# #Gold5 #Simulation #Implementation #BFS
 #얼음틀문제랑유사
# https://www.acmicpc.net/problem/16234
#------------------------

from collections import deque

def bfs(maps, L, R):
    # 상, 우, 하, 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    alliance = []
    for st_r in range(N):
        for st_c in range(N):
            # print("start", st_r, st_c)

            g = [(st_r, st_c)]
            q = deque([(st_r,st_c)])
            visited[st_r][st_c] = 1
            while q:
                r, c = q.popleft()
                # 이웃탐색: 상, 우, 하, 좌 확인
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < N and 0 <= nc < N :
                        # print("try", nr, nc, end ="->")
                        # print("visited", visited[nr][nc], end="->")
                        if L <= abs(maps[r][c] - maps[nr][nc]) <= R and visited[nr][nc] == 0:
                            # print("add queue", nr,nc)
                            visited[nr][nc] = 1
                            q.append((nr,nc))
                            g.append((nr,nc))
            if len(g) > 1:
                alliance.append(g)
    return alliance

if __name__ == '__main__':
    N, L, R = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    while True:
        visited = [[0]*N for _ in range(N)]
        alliance = bfs(maps, L, R)
        # print("alliance", alliance)
        if len(alliance) > 0:
            cnt += 1
            for a in alliance:
                total = 0
                for r, c in a:
                    total += maps[r][c]
                update = total//len(a)
                for r, c in a:
                    maps[r][c] = update
        else:
            break
        # for lst in maps: print(*lst) 
    print(cnt)

    
