#------------------------
# #Implementation #Simulation #Spiral #Efficiency
# https://www.acmicpc.net/problem/21611
#------------------------

# 중심부 기준으로 구슬 깨기. -> crackMarble
# 구슬 이동시켜 빈칸 채우기. -> moveMarble
    # 연속된 빈칸이 2개 이상인 경우?
# 4개 이상 구슬 그룹 깨기. -> crackGroup
    # 0이 나오면 멈추기. (시간 초과)
# 구슬 이동시켜 빈칸 채우기. -> moveMarble
# 4개 이상 없을 때 까지 반복.
# 구슬 복제하기. -> copyMarble
    # 구슬 복제를 위한 그룹 만들때는 상어 위치 조건 확인 필요.
    # 격자보다 구슬 복제수가 많으면 버리기. -> queue 다 비울때까지 루프 돌지 않기.
def crackMarble(d, s):
    for i in range(1,s+1):
        nr = sr + dr[d-1]*i
        nc = sc + dc[d-1]*i
        marbles[nr][nc] = 0

def moveMarble():
    sdr = [0, 1, 0, -1]
    sdc = [-1, 0, 1, 0]
    d = 0
    cnt = 0
    dist = 1
    r, c = sr, sc

    # 빈 공간 큐에 넣고, 구슬 나오면 빈 공간에 구슬 옮기기. 
    # 기존 구슬 공간은 빈 공간으로 바꾸고 큐에 넣기.
    q = deque([])
    
    stop = True
    # 멈추는 조건 중요!
    while stop:
        cnt += 1
        for _ in range(dist):
            if (r,c) == (0,0):
                stop = False
                break
            # 현재 중심부가 아니라면,
            if (r,c) != (sr,sc):
                if marbles[r][c] == 0:
                    q.append((r,c))
                    # print(q)
                else:
                    if q:
                        er, ec = q.popleft()
                        marbles[er][ec] = marbles[r][c]
                        marbles[r][c] = 0
                        q.append((r,c))
            nr = r + sdr[d]
            nc = c + sdc[d]
            
            r = nr
            c = nc
        
        if cnt == 2:
            dist += 1
            cnt = 0

        d = (d+1) % 4

def crackGroup():
    global answers
    d = 0
    cnt = 0
    dist = 1
    groups = []
    r, c = sr, sc
    group = []
    stop = True
    while stop:
        cnt += 1
        for _ in range(dist):
            # 0 만나면 그만두기. -> for, while 둘다 탈출하기.
            if (r,c) != (sr, sc) and marbles[r][c] == 0:
                # print(r, c)
                stop = False
                break
            # 빈 그룹이면 시작 위치 구슬 넣어주기.
            if not group:
                group = [(r, c)]
            nr = r + sdr[d]
            nc = c + sdc[d]
            
            # 이전 구슬과 같은가?
            if marbles[nr][nc] == marbles[r][c]:
                # 같으면 그룹에 위치 추가하기.
                group.append((nr,nc))
            else:
                if len(group) > 3 and (r,c) != (sr, sc):
                    groups.append([marbles[r][c]]+[group])
                # 이전 구슬과 달라지면 그룹 비우기.
                group = []
            r = nr
            c = nc
        
        if cnt == 2:
            dist += 1
            cnt = 0

        d = (d+1) % 4
        
        
    # 그룹 있으면 구슬 폭발 시키기
    if groups:
        for color, group in groups:
            answers += color * len(group)
            for r, c in group:
                marbles[r][c] = 0
        return True
    # 그룹 없으면 멈추기
    else:
        return False

def copyMarble():
    cnt = 0
    d = 0
    dist = 1
    r, c = sr, sc
    
    groups = []
    group = []
    stop = True
    # 그룹만들기
    while stop:
        cnt += 1
        for _ in range(dist):
            if (r,c) != (sr,sc) and marbles[r][c] == 0:
                stop = False
                break
            if not group:
                group.append((r,c))

            nr = r + sdr[d]
            nc = c + sdc[d]
            
            if marbles[nr][nc] == marbles[r][c]:
                group.append((nr,nc))
            else:
                # 움직이기 전이 중심부가 아니라면,
                if (r,c) != (sr, sc):
                    groups.append(len(group))
                    groups.append(marbles[r][c])
                group = []
            r = nr
            c = nc

        if cnt == 2:
            dist += 1
            cnt = 0

        d = (d+1)%4

    cnt = 0
    d = 0
    dist = 1
    r, c = sr, sc
    groups = deque(groups)
    # print(groups)
    stop = True
    while stop:
        cnt += 1
        for _ in range(dist):
            if (r,c) == (0,0):
                stop = False
                break
            nr = r + sdr[d]
            nc = c + sdc[d]
            
            if groups:
                marbles[nr][nc] = groups.popleft()
            else:
                marbles[nr][nc] = 0

            r = nr
            c = nc

        if cnt == 2:
            dist += 1
            cnt = 0

        d = (d+1)%4

    

from collections import deque

# 좌하우상 -> 나선형
sdr = [0, 1, 0, -1]
sdc = [-1, 0, 1, 0]

# 상하좌우 -> 구슬 깨기
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

answers = 0

N, M = map(int,input().split())
marbles = [list(map(int,input().split())) for _ in range(N)]
blizards = [list(map(int, input().split())) for _ in range(M)]
sr = sc = N//2
for d, s in blizards:
    crackMarble(d, s)
    # print("Crack marbles")
    # for row in marbles: print(*row)
    moveMarble()
    # print("Move marbles")
    # for row in marbles: print(*row)
    while True:
        if not crackGroup():
            break
        # print("crack group of marbles")
        # for row in marbles: print(*row)
        moveMarble()
        # print("move marbles")
        # for row in marbles: print(*row)
    # print("crack group of marbles")
    # for row in marbles: print(*row)
    copyMarble()
    # print("copy marbles")
    # for row in marbles: print(*row)

print(answers)

