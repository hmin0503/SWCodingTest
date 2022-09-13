#------------------------
# 치킨 배달
# #Gold5 #BruteForce #Implementation #Backtracking
# 14889와 유사
# https://www.acmicpc.net/problem/15686
#------------------------
def calculate_dist(selected):
    total_dist = 0
    for hr, hc in houses:
        minimum = 1e+9
        for sr, sc in selected:
            dist = abs(hr-sr) + abs(hc-sc)
            minimum = min(minimum, dist)
        total_dist += minimum
    return total_dist

def selection(selected, st, M):
    global min_dist
    if len(selected) == min(M, len(chickens)):
        dist = calculate_dist(selected)
        min_dist = min(min_dist, dist)
        return 

    for g in range(st, len(chickens)):
        if g not in selected:
            selected.append(chickens[g])
            selection(selected, g+1, M)
            selected.pop()



if __name__ == '__main__':
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    chickens = []
    houses = []
    selected = []
    for r in range(N):
        for c in range(N):
            if maps[r][c] == 2:
                chickens.append((r,c))
            if maps[r][c] == 1:
                houses.append((r,c))
    min_dist = 1e+9
    selection([], 0, M)
    print(min_dist)