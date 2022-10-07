#------------------------
# #BFS #Graph #Traversal #Queue #Implementation
# https://www.acmicpc.net/problem/1012
#------------------------
from collections import deque

def bfs(r,c):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    queue = deque([(r,c)])
    visited[r][c] = True

    while queue:
        sr, sc = queue.popleft()
        for i in range(4):
            nr = sr + dr[i]
            nc = sc + dc[i]
            if 0 <= nr < N and 0 <= nc < M and field[nr][nc] == 1:
                if not visited[nr][nc] :
                    visited[nr][nc] = True
                    queue.append((nr,nc))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split()) #주의, M: column(가로), M: row(세로)
        field = [[0]*M for _ in range(N)]
        visited = [[False]*M for _ in range(N)]
        for _ in range(K):
            c, r = map(int, input().split())
            field[r][c] = 1
        cnt = 0
        for r in range(N):
            for c in range(M):
                if field[r][c] == 1 and not visited[r][c]:
                    bfs(r,c)
                    cnt += 1
        print(cnt)