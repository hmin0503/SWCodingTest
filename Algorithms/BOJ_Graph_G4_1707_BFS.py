#------------------------
# #BFS #Graph #Traversal #Queue #Implementation
# https://www.acmicpc.net/problem/1707
#------------------------

if __name__=='__main__':
    K = int(input())
    for _ in range(K):
        V, E = map(int, input().split())
        graph = [[] for _ in range(V+1)]
        for _ in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        
        
