#------------------------
# #BFS #Graph #Traversal #Queue #Implementation
# https://www.acmicpc.net/problem/7569
#------------------------
from collections import deque
import sys

if __name__ == '__main__':
    M, N, H = map(int, input().split()) # 가로, 세로
    # 3차원 데이터 입력으로 시간초과 관리 필수. pypy3 & sys.stdin.readline
    field = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

    visited = [[[0] * M for _ in range(N)] for _ in range(H)]
    queue = deque([])
    total = 0
    # 익은 토마토 찾기
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if field[h][r][c] >= 0:
                    total += 1
                if field[h][r][c] == 1:
                    queue.append((h, r, c))
                    visited[h][r][c] = 1

    # 이미 다 익었으면 0 출력.
    if total == len(queue):
        print(0)
    else:
        ripe = len(queue)
        # 위, 아래, 뒤, 오른쪽, 앞, 왼쪽
        dh = [1, -1, 0, 0, 0, 0]
        dr = [0, 0, -1, 0, 1, 0]
        dc = [0, 0, 0, 1, 0, -1]
        while queue:
            h, r, c = queue.popleft()
            for i in range(len(dr)):
                nh = h + dh[i]
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<= nh < H and 0 <= nr < N and 0 <= nc < M and field[nh][nr][nc] == 0:
                    if visited[nh][nr][nc] == 0:
                        visited[nh][nr][nc] = visited[h][r][c] + 1
                        ripe += 1
                        queue.append((nh, nr, nc))

        # 주의: 토마토 숙성 후, 토마토가 다 익었는지 확인.
        if total == ripe:
            maximum = 0
            for heights in visited:
                for rows in heights:
                    maximum = max(max(rows), maximum)
            print(maximum-1)
        else:
            print(-1)




    