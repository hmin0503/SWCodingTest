#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #DFS #Graph #Traversal #Stack #Recursive
# https://www.acmicpc.net/problem/24480
#------------------------
#재귀의 깊이를 늘려주어야 recursion error가 해결된다.
import sys
sys.setrecursionlimit(10**9)

def dfs(E, R, visited, cnt = 1):
    visited[R] = cnt
    for n in E[R]:
        if visited[n] == 0:
            dfs(E, n, visited, cnt + 1)

    
def main():
    N, M, R = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    edges = [sorted(lst, reverse = True) for lst in edges]
    dfs(edges, R, visited) # Recursion Error

    for i in range(1, N+1):
        print(visited[i])
        
def main2():
    N, M, R = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    edges = [sorted(lst, reverse = False) for lst in edges] 
    # 내림차 순으로 스택에서 꺼내기 위해 미리 오름차순으로 정렬.
    
    stack = [R]
    cnt = 1
    while stack:
        s = stack.pop(-1)
        if visited[s] == 0:
            visited[s] = cnt
        for n in edges[s]:
            if visited[n] == 0:
                stack.append(n)
        cnt += 1
    for i in range(1, N+1):
        print(visited[i])

if __name__ == '__main__':
    main2()