import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split()) # row x column 입력 값
grid = [list(map(int, list(input().strip()))) for _ in range(N)] # 미로 입력 값 
visited = [[0] * M for _ in range(N)] # 해당 칸 방문 여부 확인
dr = [-1, 0, 1, 0] # 상/우/하/좌 방향으로 돌면서 움직일 수 있는 칸 확인
dc = [0, 1, 0, -1]

queue = deque([(0, 0)]) # 첫 시작 점 queue에 저장
visited[0][0] = 1 # 첫 시작 점 방문 처리

while queue:
    sr, sc = queue.popleft()
    for i in range(4):
        nr = sr + dr[i] # 4 방향 모두 확인하며, 움직일 수 있는지 확인
        nc = sc + dc[i] 
        # 미로를 벗어나지 않고 / 이동할 수 있는 칸이고 / 방문한적 없는 칸 찾기
        if (0 <= nr < N and 0 <= nc < M) and grid[nr][nc] == 1 and visited[nr][nc] == 0:
            queue.append((nr,nc)) # 조건에 해당 하면 queue에 저장하여 이후에 방문
            visited[nr][nc] = visited[sr][sc] + 1 # 현재 칸 방문 최단 거리 값 저장
print(visited[-1][-1]) # (N, M) 칸 최단 거리 출력
