import sys
input = sys.stdin.readline
from collections import deque

#---------------
# BFS 로 풀기
#---------------
def bfs(v):
    # 기준 노드로 부터 목표 노드 까지의 최단 거리 구하기
    queue = deque([v]) # 기준 노드 queue에 넣기
    visited = [-1] * (n+1) 
    visited[v] = 0 # 기준 노드 방문 처리 (본인은 0촌이라고 가정)
    while queue:
        q = queue.popleft()
        for nb in graph[q]: # 현재 노드의 이웃 노드 탐색
            if visited[nb] == -1: # 이웃 노드 방문 이전이라면 현재 노드 기준으로 촌수 입력
                queue.append(nb)
                visited[nb] = visited[q] + 1 # 현대 노드 기준으로 촌수 계산 ( = 기준 노드와의 거리 값 계산)
    return visited


#---------------
# DFS 로 풀기
#---------------
def dfs(v):
    # 기준 노드로부터 목표 노드가 나올 때 까지 탐색
    if v == b: # 목표 노드 도달 시 멈춤
        return
    for nb in graph[v]: # 현재 노드의 이웃 탐색
        if visited[nb] == -1: # 현재 노드 이웃을 방문한 적 없다면
            visited[nb] = visited[v] + 1 # 현재 노드를 기준으로 이웃 노드의 촌수 계산
            dfs(nb) # 이웃 노드 방문

n = int(input()) # 전체 사람의 수
a, b = map(int, input().strip().split()) # 촌수를 계산할 두 사람
m = int(input()) # 부모 자식들 간의 관계의 개수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().strip().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(a)[b])

visited = [-1] * (n+1)
visited[a] = 0
dfs(a)
print(visited[b])
