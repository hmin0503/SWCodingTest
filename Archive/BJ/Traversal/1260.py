#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #BFS #Graph #Traversal #Queue #Stack #DFS
# https://www.acmicpc.net/problem/1260
#------------------------

def main():
    N, M, V = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    
    for _ in range(M):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    
    # 1. stack방법으로 구현할 때 
    # - 이웃 노드 정보를 뒤에서부터 꺼내고 마지막에 꺼낸 것이 스택에 가장 상단에 위치함.
    # - 상단의 것을 pop을 할 때 visited 여부를 파악하고 방문함.
    # - 오름차 순이 되기 위해선 스택 상단에 가장 작은 숫자가 와야함.
    edges = [sorted(lst, reverse = True) for lst in edges]

    # DFS
    visited = [0] * (N+1)
    stack = [V]
    while stack:
        s = stack.pop()
        if visited[s] == 0:
            visited[s] = 1
            print(s, end = " ")
        for n in edges[s]:
            if visited[n] == 0:
                stack.append(n)
    print()
    
    # BFS
    from collections import deque
    edges = [sorted(lst, reverse = False) for lst in edges]
    visited = [0] * (N+1)
    queue = deque([V])
    visited[V] = 1
    print(V, end = " ")
    while queue:
        q = queue.popleft()
        for n in edges[q]:
            if visited[n] == 0:
                visited[n] = 1
                queue.append(n)
                print(n, end = " ")

if __name__ == "__main__":
    main()