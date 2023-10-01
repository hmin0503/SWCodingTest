import sys
input = sys.stdin.readline
from collections import deque

f, s, g, u, d = map(int, input().strip().split())
dd = [u, -d]

def bfs(v):
    visited = [-1] * (f+1)
    queue = deque([v])
    visited[v] = 0
    while queue:
        if visited[g] != -1: # 원하는 층에 대한 값을 구하면 멈추기...
            break
        q = queue.popleft()
        for i in range(2): # 위로 가는 경우, 아래로 가는 경우 탐색
            nq = q + dd[i] 
            if 1 <= nq <= f and visited[nq] == -1: # 위로 가는 경우 또는 아래로 가는 경우가 빌딩 내부일 경우, 그리고 방문한 적 없을 경우
                queue.append(nq) # queue에 넣고 다음 위치로 선정
                visited[nq] = visited[q] + 1 # 다음 위치 가기 위해 눌러야 하는 버튼 횟수 저장
    return visited
visited = bfs(s)
print(visited[g]) if visited[g] != -1 else print("use the stairs")


#---------------
# DFS로는 풀 수가 없음..! 최단 거리가 아닐 수도 있으니까?
#---------------

# def dfs(v, visited):
#     if v == g: # 원하는 층에 도달 하면 dfs 빠져나오기!
#         return
#     for i in range(2):
#         nv = v + dd[i]
#         if 1 <= nv <= f and visited[nv] == 0: # 위로 가는 경우 또는 아래로 가는 경우가 빌딩 내부일 경우, 그리고 방문한 적 없을 경우
#             visited[nv] = visited[v] + 1 # 다음 위치 가기 위해 눌러야 하는 버튼 횟수 저장
#             dfs(nv, visited) # 다음 위치로 이동하며 탐색 시작

# visited = [0]*(f+1)
# dfs(s, visited)
# print(visited[g]) if visited[g] != -1 else print("use the stairs")