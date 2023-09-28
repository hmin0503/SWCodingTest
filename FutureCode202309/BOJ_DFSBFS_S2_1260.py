import sys
from collections import deque
input = sys.stdin.readline

def bfs(V):
    q = deque([V]) # 처음 시작 지점 저장
    visited_b[V] = 1 # 처음 노드 방문 처리
    while q: # queue가 빌 때까지 while loop
        s = q.popleft() # 처음 시작 지점 pop 
        answer_b.append(s) # 방문 기록, print(s, end = " ") 로 대신해도 됨!
        for n in graph[s]: # 현재 정점을 기준으로 연결된 정점 확인
            if not visited_b[n]: # 이미 방문한 이웃 노드라면 pass 
                q.append(n) # 방문한적 없다면 queue에 저장 -> 다음에 방문할 곳
                visited_b[n] = 1 # 방문 한 곳이라고 표시(이후 중복으로 queue에 넣지 않도록!)

def dfs(V):
    visited_d[V] = 1
    for n in graph[V]:
        if not visited_d[n]:
            answer_d.append(n)
            dfs(n)

if __name__ == '__main__':
    N, M, V = map(int, input().strip().split())
    graph = [[] for _ in range(N+1)] # 인접 리스트로 그래프 표현
    for _ in range(M):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        graph[b].append(a)
    graph = [sorted(edge) for edge in graph] # 낮은 숫자 부터 방문

    visited_b = [0] * (N+1) # bfs 방문 기록
    visited_d = [0] * (N+1) # dfs 방문 기록
    answer_b = []   # bfs 방문 순서 기록
    answer_d = [V]  # dfs 방문 순서 기록

    dfs(V)
    print(*answer_d)

    bfs(V)
    print(*answer_b)