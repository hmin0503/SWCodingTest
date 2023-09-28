import sys
input = sys.stdin.readline

r, c = map(int, input().strip().split())
graph = [list(input().strip()) for _ in range(r)] # 구슬 맵


visited_r = [[0] * (c+1) for _ in range(r+1)] # 빨간 구슬 방문 여부 확인
visited_b = visited_r.copy() # 파란 구슬 방문 여부 확인

queue = [] # 현재 구슬들의 위치
###### 230928 에 풀다가 쉬운 문제로 넘어감 ㅠ ######