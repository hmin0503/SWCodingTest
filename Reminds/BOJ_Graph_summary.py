# https://www.acmicpc.net/problem/24479
# 알고리즘 수업 - 깊이 우선 탐색 1
# dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#         if (visited[x] = NO) then dfs(V, E, x);
# }

"""
Input:
5 5 1
1 4
1 2
2 3
2 4
3 4

Output:
1
2
3
4
0
"""

import sys
sys.setrecursionlimit(10**9)

# list는 외부 전역변수로 두어도 함수 내에서 변경이 가능해.
def dfs(s):
    global cnt
    visited[s] = cnt
    for n in graph[s]:
        if visited[n] == 0 :
            cnt += 1
            dfs(n)

if __name__ == '__main__':
    N, M, R = map(int,input().split())
    graph = {i:[] for i in range(1, N+1)}
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0] * (N+1)

    #오름차순 방문 -> 내림차순 정렬
    graph = {k:sorted(v, reverse = False) for k,v in graph.items()}
    cnt = 1
    dfs(R)

    for i in visited[1:]:
        print(i)

# https://www.acmicpc.net/problem/24480
# 알고리즘 수업 - 깊이 우선 탐색 2
# dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 내림차순으로 방문한다)
#         if (visited[x] = NO) then dfs(V, E, x);
# }

"""
Input:
5 5 1
1 4
1 2
2 3
2 4
3 4

Output:
1
4
3
2
0
"""

def dfs(v):
    global count
    visited[v] = count
    graph[v].sort(reverse = True)
    for g in graph[v]:
        if visited[g] == 0:
            count += 1
            dfs(g)

import sys
sys.setrecursionlimit(10**9)
if __name__ == "__main__":
    input = sys.stdin.readline

    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    count = 1

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    dfs(r)

    for i in range(1, n + 1):
        print(visited[i])

# https://www.acmicpc.net/problem/24444
# 알고리즘 수업 - 너비 우선 탐색 1
# bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     for each v ∈ V - {R}
#         visited[v] <- NO;
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
#     while (Q ≠ ∅) {
#         u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
#         for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#             if (visited[v] = NO) then {
#                 visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
#                 enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
#             }
#     }
# }
"""
Input:
5 5 1
1 4
1 2
2 3
2 4
3 4

Output:
1
2
4
3
0
"""
from collections import deque
import sys

if __name__ == '__main__':
    N, M, R = map(int,input().split())
    graph = {i:[] for i in range(1, N+1)}
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [0] * (N+1)
    #오름차순 방문 -> 내림차순 정렬
    graph = {k:sorted(v, reverse = False) for k,v in graph.items()}

    # BFS
    cnt = 1
    visited[R] = cnt
    queue = deque([R])
    while queue:
        q = queue.popleft()
        for n in graph[q]:
            if visited[n] == 0:
                cnt += 1
                visited[n] = cnt
                queue.append(n)
    
    for i in visited[1:]:
        print(i)

# https://www.acmicpc.net/problem/24445
# 알고리즘 수업 - 너비 우선 탐색 1
# bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     for each v ∈ V - {R}
#         visited[v] <- NO;
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
#     while (Q ≠ ∅) {
#         u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
#         for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 내림차순으로 방문한다)
#             if (visited[v] = NO) then {
#                 visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
#                 enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
#             }
#     }
# }
"""
Input:
5 5 1
1 4
1 2
2 3
2 4
3 4

Output:
1
3
4
2
0
"""
import sys
from collections import deque
if __name__ == '__main__':
    N, M, R = map(int, input().split())
    edges = {i:[] for i in range(1, N+1)}
    visited = [0] * (N+1)
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        edges[u].append(v)
        edges[v].append(u)
    edges = {k:sorted(v, reverse = True) for k,v in edges.items()}
    
    cnt = 1
    visited[R] = cnt
    queue = deque([R])
    while queue:
        q = queue.popleft()
        for n in E[q]:
            if visited[n] == 0:
                cnt += 1
                visited[n] = cnt
                queue.append(n)

    print(*visited[1:], sep = "\n")

# https://www.acmicpc.net/problem/2667
# 단지번호붙이기
"""
Input: 
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

Output:
3
7
8
9
"""
# BFS로 풀기
from collections import deque
def bfs(r,c):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    cnt = 1
    queue = deque([(r,c)])
    visited[r][c] = True

    while queue:
        sr, sc = queue.popleft()
        for i in range(4):
            nr = sr + dr[i]
            nc = sc + dc[i]
            if 0<=nr<N and 0<=nc<N and town[nr][nc] == '1':
                if not visited[nr][nc] :
                    cnt += 1
                    visited[nr][nc] = True
                    queue.append((nr,nc))
    return cnt

if __name__ == '__main__':
    N = int(input())
    town = [list(input()) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    cnts = []
    for r in range(N):
        for c in range(N):
            if town[r][c] == '1' and not visited[r][c]:
                cnts.append(bfs(r,c))
    cnts = sorted(cnts)

    print(len(cnts))
    for c in cnts: print(c)

# DFS로 풀기
def dfs(maps, r, c):
    global cnt
    if c <= -1 or c >= len(maps) or r <= -1 or r >= len(maps):
        return False
    
    if maps[r][c] == 1:
        cnt += 1
        maps[r][c] = 0
        dfs(maps, r-1, c) # 상
        dfs(maps, r, c-1) # 좌
        dfs(maps, r+1, c) # 하
        dfs(maps, r, c+1) # 우
        return True
    return False

import sys
sys.setrecursionlimit(10**9)
if __name__ == '__main__':
    N = int(input())
    maps = [list(map(int, list(input()))) for _ in range(N)]
    result = 0
    cnt = 0
    answers = []
    for r in range(N):
        for c in range(N):
            if dfs(maps, r, c) == True :
                answers.append(cnt)
                result += 1
                cnt = 0 
    print(result)
    print(*sorted(answers), sep = "\n") #오름차순 정렬 후 출력


# https://www.acmicpc.net/problem/1697
# 숨바꼭질 
from collections import deque
if __name__ == '__main__':
    N, K = map(int, input().split())
    visited = [0] * 100001 # 주의
    queue = deque([N])
    visited[N] = 1

    while queue:
        q = queue.popleft()
        
        # 1초 후 한칸 이동
        nq = q + 1
        if 0 <= nq < 100001 and visited[nq] == 0:  # 주의
            visited[nq] = visited[q] + 1
            queue.append(nq)
        # 1초 후 한칸 이동
        nq = q - 1
        if 0 <= nq < 100001 and visited[nq] == 0:  # 주의
            visited[nq] = visited[q] + 1
            queue.append(nq)

        # 1초 후 두 배 이동
        nq = q*2
        if 0 <= nq < 100001 and visited[nq] == 0:  # 주의
            visited[nq] = visited[q] + 1
            queue.append(nq)
    print(visited[K]-1)


# https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기
"""
Input:
6 4
0100
1110
1000
0000
0111
0000
Output:
15
"""
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


# 이분 그래프
# https://www.acmicpc.net/problem/1707
"""
Input: 
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
Output:
YES
NO
"""
from collections import deque
def bfs(start):        
    queue = deque([start])
    visited[start] = 1
    while queue:
        q = queue.popleft()
        for n in graph[q]:
            # 방문한적 없다면 번호 부여.
            if visited[n] == 0:
                queue.append(n)
                visited[n] = visited[q]*-1
            # 방문한적 있다면 기존 번호와 현재 번호 비교. 같으면 NO.
            elif visited[n] == visited[q]:
                return False
    return True

if __name__=='__main__':
    K = int(input())
    for _ in range(K):
        V, E = map(int, input().split())

        graph = [[] for _ in range(V+1)]
        visited = [0] * (V+1)
        flag = "YES"

        for _ in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        for i in range(1, V+1):
            if visited[i] == 0:
                if not bfs(i):
                    flag = "NO"
                    break
        print(flag)

# https://www.acmicpc.net/problem/7576
# 토마토 
# 시작점이 여러개인 BFS
"""
Input:
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1

Output:
6
"""
from collections import deque

if __name__ == '__main__':
    M, N = map(int, input().split()) # 가로, 세로
    # 0: 익지 않은 토마토, 1: 익은 토마토, -1: 토마토 없는 칸
    field = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    queue = deque([])
    total = 0

    # 익은 토마토 모두 찾아서 queue에 넣고 BFS.
    for r in range(N):
        for c in range(M):
            if field [r][c] >= 0:
                total += 1
            if field[r][c] == 1:
                queue.append((r,c))
                visited[r][c] = 1

    if total == len(queue):
        print(0)
    else:
        ripe = len(queue)
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        while queue:
            r, c = queue.popleft()

            # 익은 토마토 상우좌하에 영향 미치기.
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M and field[nr][nc] == 0:
                    if visited[nr][nc] == 0:
                        visited[nr][nc] = visited[r][c] + 1
                        ripe += 1
                        queue.append((nr,nc))
        if total == ripe:
            maximum = 0
            for rows in visited:
                maximum = max(max(rows), maximum)
            print(maximum-1)
        else:
            print(-1)