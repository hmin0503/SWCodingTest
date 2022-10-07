#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #BFS #Graph #Traversal #Queue
# https://www.acmicpc.net/problem/2606
#------------------------

def bfs(G, R, visited):
    from collections import deque
    answer = 0 # 추가로 바이러스 걸릴 컴퓨터 수
    queue = deque([R])
    visited[R] = 1
    
    while queue:
        q = queue.popleft()
        for n in G[q]:
            if visited[n] == 0:
                answer += 1
                queue.append(n)
                visited[n] = 1
    return answer
    
def main():
    N = int(input())
    E = int(input())
    edges = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    
    visited = [0] * (N+1)
    print(bfs(edges, 1, visited))
    

if __name__ == '__main__':
    main()
