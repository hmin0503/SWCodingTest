#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #BFS #Graph #Traversal #Queue
# https://www.acmicpc.net/problem/24445
#------------------------
def bfs(E, R, visited):
    from collections import deque
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
                
def main():
    import sys
    N, M, R = map(int, input().split())
    edges = {i:[] for i in range(1, N+1)}
    visited = [0] * (N+1)
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split()) # 시간초과로 sys.stdin.readline으로 변경.
        edges[u].append(v)
        edges[v].append(u)
    edges = {k:sorted(v, reverse = True) for k,v in edges.items()}
    
    bfs(edges, R, visited)
if __name__ == '__main__':
    main()