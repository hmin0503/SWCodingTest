#------------------------
# #BFS #Graph #Traversal #Queue #Implementation
# https://www.acmicpc.net/problem/2206
#------------------------
from collections import deque

if __name__ == '__main__':
    N, M = map(int, input().split())
    maps = [list(map(int, list(input()))) for _ in range(N)]

    visited = [[[0,0] for _ in range(M)] for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    queue = deque([(0,0,0)])
    visited[0][0][0] = 1
    while queue:
        r, c, b = queue.popleft()
        for i in range(len(dr)):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if maps[nr][nc] == 0:
                    if visited[nr][nc][b] == 0:
                        visited[nr][nc][b] = visited[r][c][b] + 1
                        queue.append((nr, nc, b))

                # 한 칸 정도는 부수기. -> 그래프를 따로 구성?
                elif maps[nr][nc] == 1 and b == 0:
                    b = 1
                    nr = nr + dr[i]
                    nc = nc + dc[i]
                    if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] == 0:
                        if visited[nr][nc][b] == 0:
                            visited[nr][nc][b] = visited[r][c][0] + 1
                            queue.append((nr, nc, b))
    for lst in visited: print(lst)
    if visited[-1][-1][0] != 0 or visited[-1][-1][-1] != 0:                  
        print(visited[-1][-1])
    else:
        print(-1)
