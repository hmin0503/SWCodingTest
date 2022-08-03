#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #BFS #Graph #Traversal #Queue
# https://www.acmicpc.net/problem/24444
#------------------------
def bfs(E, R, visited):
    from collections import deque
    print(R)
    visited[R] = 1
    queue = deque([R])
    while queue:
        q = queue.popleft()
        for n in E[q]:
            if visited[n] == 0:
                print(n)
                visited[n] = 1
                queue.append(n)
                
def main():
    N, M, R = map(int, input().split())
    edges = {i:[] for i in range(1, N+1)}
    visited = [0] * (N+1)
    for _ in range(M):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    edges = {k:sorted(v, reverse = False) for k,v in edges.items()}
    
    bfs(edges, R, visited)
    print(0)
if __name__ == '__main__':
    main()