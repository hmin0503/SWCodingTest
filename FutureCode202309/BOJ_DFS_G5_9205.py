import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    visited = [0] * (n+2)
    queue = deque([[hx, hy]])
    while queue:
        sx, sy = queue.popleft()
        if abs(sx-fx) + abs(sy-fy) <= 1000: # 현재 위치(집 or 편의점)에서 축제까지 거리가 1000m 이하이면 happy~, 집과 편의점에서는 맥주가 20개 이기 때문
            print("happy")
            return
        for i in range(n): # 다음 편의점에 방문한 적 없다면, 방문 해보기
            if visited[i] == 0:
                nx, ny = conv[i]
                # 다음 편의점 까지의 거리가 1000 이하라면 방문하기
                if abs(sx - nx) + abs(sy - ny) <= 1000:
                    queue.append([nx, ny])
                    visited[i] = 1
    print("sad") # 그 어떤 편의점도 가지 못하고, 축제까지도 못 갔기 때문에 sad
    return

t = int(input())
for _ in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    conv = [list(map(int, input().split())) for _ in range(n)]
    fx, fy = map(int, input().split())
    bfs()









