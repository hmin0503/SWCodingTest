#-----------------------------------------------
# 치킨 배달 G5 # DFS(중복없는 N개 중 M개 조합 구하기)
# https://www.acmicpc.net/problem/15686
#-----------------------------------------------
# 치킨 거리 최소값 구하기 -> DFS
# 중복 없이 조합 구하기 -> 시간 초과 잡기
#-----------------------------------------------

def dfs(loc, st):
    global answers
    if len(loc) == M:
        total_dist = 0
        for hr, hc in houses:
            minimum = 1e9
            for fr, fc in loc:
                dist = abs(fr-hr) + abs(fc-hc)
                minimum = min(minimum, dist)
            total_dist += minimum
        answers = min(answers, total_dist)
        return

    # 시간초과 잡기
    for i in range(st, len(franchises)):
        if franchises[i] not in loc:
            loc.append(franchises[i])
            dfs(loc, i + 1)
            loc.pop()


answers = 1e9
N, M = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]
franchises = [] 
houses = []
for r in range(N):
    for c in range(N):
        if cities[r][c] == 2:
            franchises.append((r,c))
        if cities[r][c] == 1:
            houses.append((r,c))
dfs([], 0)
print(answers)