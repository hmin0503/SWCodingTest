import sys
sys.setrecursionlimit(10**9)

def dfs(V,E,R):
    global cnt
    V[R] = cnt
    for v in E[R]:
        if V[v] == 0:
            cnt += 1
            dfs(V,E,v)


if __name__ == '__main__':
    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    graph = [sorted(g, reverse = False) for g in graph]
    visited=[0]*(N+1)
    cnt = 1
    visited[R] = cnt
    dfs(visited, graph, R)
    for v in visited: print(v)