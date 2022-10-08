#------------------------
# #BFS #Graph #Traversal #Queue #Implementation
# https://www.acmicpc.net/problem/2206
#------------------------
from collections import deque
def bfs():
    queue = deque([1])
    visited[1] = 1
    while queue:
        i = queue.popleft()
        if i == 100:
            return board[i]

        for d in range(1,7):
            ni = i + d
            if 0 <= ni < 101 and visited[ni] == 0:
                # 사다리나 뱀이 있는지 확인하기. 
                if ni in ladders:
                    ni = ladders[ni]
                elif ni in snakes:
                    ni = snakes[ni]
                else:
                    ni = ni
                if visited[ni] == 0:
                    visited[ni] = 1
                    board[ni] = board[i] + 1
                    queue.append(ni)
    return -1

if __name__ == '__main__':
    N, M = map(int, input().split())

    ladders = {}
    snakes = {}
    for _ in range(N):
        x, y = map(int, input().split())
        ladders[x] = y
    for _ in range(M):
        u, v = map(int, input().split())
        snakes[u] = v

    visited = [0] * 101
    # 틀린 이유: 방문과 주사위 굴린 횟수는 따로 저장
    board = [0] * 101
    print(bfs())