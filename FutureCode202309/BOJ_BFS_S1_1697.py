
from collections import deque
import sys;
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0]*100001

queue = deque([N])
visited[N] = 1
while queue:
    q = queue.popleft()

    nq = q - 1
    if 0 <= nq <= 100000 and visited[nq] == 0:
        queue.append(nq)
        visited[nq] =  visited[q] + 1
    
    nq = q + 1
    if 0 <= nq <= 100000 and visited[nq] == 0:
        queue.append(nq)
        visited[nq] = visited[q] + 1

    nq = 2 * q
    if 0 <= nq <= 100000 and visited[nq] == 0:
        queue.append(nq)
        visited[nq] = visited[q] + 1
print(visited[K]-1)
