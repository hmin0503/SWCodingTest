#------------------------
# #BFS #Graph #Traversal #Queue #Implementation
# https://www.acmicpc.net/problem/7562
#------------------------
from collections import deque

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        L = int(input())
        sr, sc = map(int, input().split())
        er, ec = map(int, input().split())
        visited = [[0]*L for _ in range(L)]
        # 1시,2시, 4시,5시, 7시,8시, 10시,11시
        dr = [-2, -1, 1, 2, 2, 1, -1, -2]
        dc = [1, 2, 2, 1, -1, -2, -2, -1]
        queue = deque([(sr,sc)])
        visited[sr][sc] = 1
        while queue:
            if visited[er][ec] != 0 : # 시간초과 관리.
                break
            r, c = queue.popleft()
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < L and 0 <= nc < L and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr,nc))
        print(visited[er][ec]-1)



    