#------------------------
# #Implementation #Simulation #Efficiency #BFS
# https://www.acmicpc.net/problem/21609
#------------------------

# 연결된 블록집합 구하기 -> getGroups -> BFS
    # 그룹에 속한 블록 개수는 2개 이상.
    # 무조건 일반 블록 1개 이상 포함.
    # 기준 블록은 행의 번호 가장 작고, 열 번호가 가장 작은 것.
    # 무지개 블록 따로 저장해서 방문 처리 해제
    # 그룹 저장할때 그룹 크기, 무지개 개수 포함하기

# 가장 큰 블록 그룹. -> Sorting
    # 무지개 블록 수가 많은 그룹
    # 기준 블록 행이 가장 큰 그룹
    # 기준 블록 열이 가장 큰 그룹

# 가장 큰 블록 제거. 점수 획득.

# 중력 작용. -> 아래로 계속 이동.
    # 검은 블록은 그대로 고정.

# 반시계 90도 회전.

# 중력 작용.
    # 검은 블록은 그대로 고정.

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

def getGroups(sr,sc, visited):
    # 상우하좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    visited[sr][sc] = 1
    queue = deque([(sr,sc)])
    color = blocks[sr][sc]
    group = [(sr,sc)]
    rainbow = []
    while queue:
        r,c = queue.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 0 : 
                    if blocks[nr][nc] == color or blocks[nr][nc] == 0:
                        visited[nr][nc] = 1
                        queue.append((nr,nc))
                        if blocks[nr][nc] == color:
                            group.append((nr,nc))
                        if blocks[nr][nc] == 0:
                            rainbow.append((nr,nc))

    for r, c in rainbow:
        visited[r][c] = 0
    group = sorted(group, key = lambda x:(x[0],x[1]))
    return [len(group)+len(rainbow), len(rainbow), group+rainbow]

def gravity():
    for r in range(N-2,-1,-1):
        for c in range(N):
            if blocks[r][c] >= 0:
                for nr in range(r+1, N):
                    if blocks[nr][c] == -2:
                        blocks[nr][c], blocks[nr-1][c] = blocks[nr-1][c], blocks[nr][c]
                    else:
                        break
                    
from collections import deque
if __name__ == "__main__":
    answers = 0

    N, M = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(N)]
    while True:
        
        # 블록 그룹 구하기
        groups = []
        visited = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if blocks[r][c] > 0 and visited[r][c] == 0 :
                    group = getGroups(r,c, visited)
                    if group[0] > 1:
                        groups.append(group)
        if not groups:
            break
        # 가장 큰 그룹 구하기
        groups = sorted(groups, key = lambda x: (x[0], x[1], x[2][0][0], x[2][0][1]), reverse = True)
        # 점수 획득
        answers += groups[0][0]**2
        # 가장 큰 그룹 제거
        for r, c in groups[0][2]:
            blocks[r][c] = -2
        # print("Delete")
        # for row in blocks: print(*row)
        # 중력 작용
        gravity()
        # print("Gravity")
        # for row in blocks: print(*row)

        # 반시계 90도 회전
        blocks = list(map(list, zip(*blocks)))[::-1]
        # print("Rotate")
        # for row in blocks: print(*row)

        # 중력 작용
        gravity()
        # print("Gravity2")
        # for row in blocks: print(*row)
    print(answers)