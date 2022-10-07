#------------------------
# #BFS #Graph #Traversal #Queue #Implementation #최단경로 #shortest #shortcut
# https://www.acmicpc.net/problem/2178
#------------------------
from collections import deque
if __name__ == '__main__':
    N, K = map(int, input().split())
    visited = [0] * 100001 # 범위 조정 주의! 
    queue = deque([N])
    visited[N] = 1

    while queue:
        q = queue.popleft()
        nq = q + 1
        if 0 <= nq < 100001 and visited[nq] == 0:  # 범위 조정 주의! 
            visited[nq] = visited[q] + 1
            queue.append(nq)
        nq = q - 1
        if 0 <= nq < 100001 and visited[nq] == 0:  # 범위 조정 주의! 
            visited[nq] = visited[q] + 1
            queue.append(nq)
        nq = q*2
        if 0 <= nq < 100001 and visited[nq] == 0:  # 범위 조정 주의! 
            visited[nq] = visited[q] + 1
            queue.append(nq)
    print(visited[K]-1)