#------------------------
# #BFS #Graph #Traversal #Queue #Implementation
# https://www.acmicpc.net/problem/1707
#------------------------
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
        # 틀린 이유: 모든 정점에 대해서 탐색하는 것이 필요. -> 비연결 그래프가 존재할 수 있음.
        for i in range(1, V+1):
            if visited[i] == 0:
                if not bfs(i):
                    flag = "NO"
                    break
        print(flag)

        
