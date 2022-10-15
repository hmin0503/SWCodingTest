#------------------------
# #Implementation #Simulation #Efficiency #DFS #BFS
# https://www.acmicpc.net/problem/21609
#------------------------
"""
TEST CASE 1
5 4
1 0 -1 0 0
2 0 -1 0 0
3 0 -1 0 0
4 0 -1 -1 -1
4 4 1 1 1
ANSWER 58
"""
"""
TEST CASE 2
5 3
0 0 0 0 1
-1 -1 0 -1 0
-1 -1 3 -1 -1
-1 -1 0 -1 -1
0 0 2 0 0
ANSWER 74
"""
"""
TEST CASE 3
4 2
1 2 0 1
0 -1 -1 -1
1 0 -1 1
2 0 0 -1
ANSWER 40
"""
def dfs(maps, color, r, c):
    global group, visited
    if 0 > r or r >= len(maps) or 0 > c or c >= len(maps[0]):
        return False
    
    # if (maps[r][c] == color or maps[r][c] == 0) and visited[r][c] == 0:
    if (maps[r][c] == color or maps[r][c] == 0) and visited[r][c] == 0:
        visited[r][c] = 1
        group.append((r,c, maps[r][c]))
        if maps[r][c] == 0:
            rainbow.append((r,c))
        dfs(maps, color, r-1, c) # 북
        dfs(maps, color, r, c+1) # 동
        dfs(maps, color, r+1, c) # 남
        dfs(maps, color, r, c-1) # 서
        return True
    return False

def gravity(maps):
    for sr in range(len(maps)-1, -1, -1):
        for sc in range(len(maps[0])):
            if maps[sr][sc] >= 0:
                r, c = sr, sc
                while True:
                    nr = r + 1
                    nc = c
                    if 0 <= nr < len(maps):
                        if maps[nr][nc] == -2:
                            r, c = nr, nc
                        else:
                            break
                    else:
                        break
                maps[r][c], maps[sr][sc] = maps[sr][sc], maps[r][c]
    return maps

if __name__ =="__main__":
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    answers = 0

    # 1. 크기가 가장 큰 그룹 찾기.
    while True:
        groups = []
        visited = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                rainbow = []
                group = []
                if maps[r][c] > 0:
                    color = maps[r][c]
                    if dfs(maps, color, r, c):
                        if len(group) > 1:
                            newGroup = []
                            for r, c, color in group:
                                newGroup.append((r,c,color,len(rainbow)))
                            groups.append(newGroup)
                for r, c in rainbow:
                    visited[r][c] = 0
        
        if len(groups) == 0:
            break

        # 1.2 크기가 같은 그룹이 여러 개면, -> 무지개 블록 많은 그룹. -> 기준 블록 행이 가장 크고, 열이 가장 큰 것.
        # 조건 정확하게 이해하기!!!
        groups = [sorted(row, key = lambda x:(-x[-2], x[0], x[1])) for row in groups]
        groups = sorted(groups, key = lambda x:(len(x), x[1][-1], x[1][0],x[1][1]), reverse = True)
        
        print(groups)
        
        # 2. 블록 제거 및 점수 획득.
        print(len(groups[0])**2)
        answers += len(groups[0])**2
        for r, c, _, _ in groups[0]:
            maps[r][c] = -2
        print("Delete")
        for row in maps: print(*row)
        
        # 3. 중력 작용. -> 아래로 블록이 다 떨어짐.
        maps = gravity(maps)
        print("Gravity1")
        for row in maps: print(*row)

        # 4. 반시계 90도 회전.
        # tmp = zip(*reversed(maps)) # 시계 90도 회전.
        maps = list(map(list, zip(*maps)))[::-1]
        print("Rotate")
        for row in maps: print(*row)

        # 5. 중력 작용.
        maps = gravity(maps)
        print("Gravity2")
        for row in maps: print(*row)

    print(answers)
