#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #BFS #Graph #Traversal #Queue #DFS #미로탐색
# https://www.acmicpc.net/problem/2178
#------------------------
def bfs(maps, r, c):
    from collections import deque
    
    # 상좌하우
    dc = [0, -1, 0, 1]
    dr = [-1, 0, 1, 0]
    
    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        # 미로는 직사각형이다.
        for ddr, ddc in zip(dr, dc):
            nr = r + ddr
            nc = c + ddc
            if nr <= -1 or nr >= len(maps) or nc <= -1 or nc >= len(maps[0]):
                continue

            # 첫 방문인 경우에만 최단 거리 기록
            if maps[nr][nc] == 1:
                maps[nr][nc] = maps[r][c] + 1
                queue.append((nr,nc))
                
    return maps[-1][-1]

def main():
    N, M = map(int, input().split())
    maps = [list(map(int, list(input()))) for _ in range(N)]
    print(bfs(maps, 0, 0))

if __name__ == '__main__':
    main()