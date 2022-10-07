#------------------------
# #BFS #Graph #Traversal #Queue #Implementation
# https://www.acmicpc.net/problem/2206
#------------------------
from collections import deque

def bfs():
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    queue = deque([(0,0,0)])
    visited[0][0][0] = 1
    while queue:
        r, c, b = queue.popleft()
        if r == N-1 and c == M-1:
            return visited[r][c][b]
        for i in range(len(dr)):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if maps[nr][nc] == 0 and visited[nr][nc][b] == 0:
                    visited[nr][nc][b] = visited[r][c][b] + 1
                    queue.append((nr, nc, b))

                # 한 칸 정도는 부수기, 벽 있는 자리에 위치. -> 그래프를 따로 구성?
                # 틀린 이유: 벽을 뛰어넘으려고 함.
                elif maps[nr][nc] == 1 and b == 0:
                    # b = 1 # 틀린 이유: b를 1이라고 명시하면 다음 방향에도 적용되어 잘못된 방법.
                    visited[nr][nc][b+1] = visited[r][c][b] + 1
                    queue.append((nr, nc, b+1))
    return -1

if __name__ == '__main__':
    N, M = map(int, input().split())
    maps = [list(map(int, list(input()))) for _ in range(N)]

    visited = [[[0,0] for _ in range(M)] for _ in range(N)]
    print(bfs())