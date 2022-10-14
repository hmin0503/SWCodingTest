#------------------------
# #Implementation #Simulation #Efficiency #DFS #BFS
# https://www.acmicpc.net/problem/23290
#------------------------

def moveFish(fish):
    # 0,  1, 2, 3, 4,  5,  6, 7
    # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
    dr = [0, -1, -1, -1, 0, 1, 1, 1]
    dc = [-1, -1, 0, 1, 1, 1, 0, -1]
    newFish = {}
    
    for k, v in fish.items():
        for r, c, d in v:
            nd = d
            while True:
                nr = r + dr[nd]
                nc = c + dc[nd]
                # 이동 후 범위 안에 있는가? 상어가 없는가? 또는 물고기 냄새가 없는가?
                if 0 < nr < 5 and 0 < nc < 5 and maps[nr][nc] == 0:
                    if (nr, nc) in newFish:
                        newFish[(nr,nc)].append((nr,nc,nd))
                    else:
                        newFish[(nr,nc)] = [(nr,nc,nd)]
                    break
                else:
                    # 회전 후 방향 제대로 넣기...!
                    nd = (nd-1)%8
                    if d == nd:
                        if (r,c) in newFish:
                            newFish[(r,c)].append((r,c,d))
                        else:
                            newFish[(r,c)] = [(r,c,d)]
                        break
    return newFish

def findCandidate(move, sr, sc):
    if len(move) == 3:
        moves.append(move[:]) # 리스트 아예 복제해서 넣어야 함...
        return
    # 상어 방향 찾기.
    for i in range(4):
        nr = sr + dr[i]
        nc = sc + dc[i]
        #  이동 가능 한가?
        if 0 < nr < 5 and 0 < nc < 5:
            move.append(i)
            findCandidate(move, nr, nc)
            move.pop()

def findMaximum(fish, moves, sr, sc, s):
    maximum = -1e9
    for move in moves:
        total = 0
        r, c = sr, sc
        tmpFish = deepcopy(fish)
        for d in move:
            r += dr[d]
            c += dc[d]
            # 물고기를 중복으로 잡지 않도록하기.
            if (r,c) in tmpFish:
                total += len(tmpFish[(r,c)])
                tmpFish[(r,c)] = []
        if maximum < total :
            maximum = total
            final = move
    for d in final:
        sr += dr[d]
        sc += dc[d]
        if (sr, sc) in fish: 
            fish[(sr,sc)] = []
            maps[sr][sc] = s
    return fish, maps, sr, sc

def deleteFishScent(maps, s):
    for r in range(1, 5):
        for c in range(1, 5):
            if maps[r][c] == s-2:
                maps[r][c] = 0
    return maps

from copy import deepcopy

if __name__ == '__main__':
    M, S = map(int, input().split())
    # 상어:1, 물고기냄새:2
    maps = [[0]*5 for _ in range(5)]
    fish = {}
    for _ in range(M):
        r, c, d = map(int, input().split())
        d -= 1
        if (r,c) in fish:
            fish[(r,c)].append((r,c,d))
        else:
            fish[(r,c)] = [(r,c,d)]

    sr, sc = map(int, input().split())
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    for s in range(1, S+1):
        # 1. 물고기 복제
        copyFish = deepcopy(fish)
        # 2. 물고기 한 칸 이동.
        fish = moveFish(fish)
        # 3. 상어 연속 3칸 이동.
        moves = []
        findCandidate([], sr, sc)
        fish, maps, sr, sc = findMaximum(fish, moves, sr, sc, s)
        # 4. 물고기 냄새 제거.
        maps = deleteFishScent(maps, s)
        # 5. 물고기 복제 완료.
        for k, v in copyFish.items():
            if k in fish:
                fish[k].extend(v)
            else:
                fish[k] = v
    answers = 0
    for k, v in fish.items():
        answers += len(v)
    print(answers)