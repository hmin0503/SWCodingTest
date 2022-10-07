#------------------------
# #BFS #Graph #Traversal #Queue #Implementation
# https://www.acmicpc.net/problem/7576
#------------------------
from collections import deque

if __name__ == '__main__':
    M, N = map(int, input().split()) # 가로, 세로
    field = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    queue = deque([])
    total = 0
    # 익은 토마토 찾기
    for r in range(N):
        for c in range(M):
            if field[r][c] >= 0:
                total += 1
            if field[r][c] == 1:
                queue.append((r,c))
                visited[r][c] = 1

    # 이미 다 익었으면 0 출력.
    if total == len(queue):
        print(0)
    else:
        ripe = len(queue)
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M and field[nr][nc] == 0:
                    if visited[nr][nc] == 0:
                        visited[nr][nc] = visited[r][c] + 1
                        ripe += 1
                        queue.append((nr,nc))

        # 주의: 토마토 숙성 후, 토마토가 다 익었는지 확인.
        if total == ripe:
            maximum = 0
            for rows in visited:
                maximum = max(max(rows), maximum)
            print(maximum-1)
        else:
            print(-1)




    