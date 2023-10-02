import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) # 재귀 한도 1000000로 올려줌

def dfs(V, dep): # 반복적으로 해당 노드를 따라서 계속 탐색
    r, c = V
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 탐색하고자 하는 노드가 범위 내에 있고, 높이 조건이 맞고, 방문한적 없다면
        # 계속 따라서 탐색 
        if (0 <= nr < N and 0 <= nc < N) and grid[nr][nc] > dep and visited[nr][nc] == 0:
            visited[nr][nc] = cnt
            dfs([nr, nc], dep)
    
N = int(input())
grid = [list(map(int, input().strip().split())) for _ in range(N)]
maxH = max([max(g) for g in grid]) # 현재 맵에서 가장 높은 곳 찾기

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
answer = []
# 모든 높이에 대해서 탐색하여 안전한 영역의 최대 개수 출력
for dep in range(maxH): # 높이에 대해서 한번씩 탐색
    visited = [[0]*(N) for _ in range(N)]   
    cnt = 0
    # 모든 위치에서 시작점 확인하기
    for r in range(N):
        for c in range(N):
            # 높이 조건에 맞고, 방문한 적이 없다면 해당 위치를 시작으로 탐색
            if grid[r][c] > dep and visited[r][c] == 0:
                cnt += 1
                visited[r][c] = 1
                dfs([r,c], dep)
    answer.append(cnt)
# 안전한 영역의 최대 개수 출력
print(max(answer))