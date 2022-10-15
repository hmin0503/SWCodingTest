#------------------------
# #Implementation #Simulation #DFS #다른사람풀이
# https://ryu-e.tistory.com/107
# https://www.acmicpc.net/problem/23290
#------------------------

def moveFish():
    res = [[[] for _ in range(5)] for _ in range(5)]
    for r in range(1, 5):
        for c in range(1, 5):
            while copyFishLocs[r][c]:
                d = copyFishLocs[r][c].pop()
                # for i in range(8):
                    # nd = (d-i)%8
                for nd in range(d, d-8, -1):
                    nd %= 8
                    nr, nc = r + ddr[nd], c + ddc[nd]
                    # if s == 3:
                    #     print(r,c,d, "->", nr, nc, nd, "|", fishSmell[nr][nc])
                    if (nr, nc) != (sr,sc) and \
                         0 < nr < 5 and 0 < nc < 5 and \
                            fishSmell[nr][nc] == 0:

                        res[nr][nc].append(nd)
                        break
                else:
                    res[r][c].append(d)

    return res

def moveShark(r, c, dep, cnt, visit):
    global maximum, sr, sc, eaten
    if dep == 3:
        if maximum < cnt:
            maximum = cnt
            sr, sc = r, c
            eaten = visit[:]
        return
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 < nr < 5 and 0 < nc < 5:
            # 방문 안한 곳이면 방문 표시 후 다음으로.
            if (nr, nc) not in visit:
                visit.append((nr,nc))
                moveShark(nr, nc, dep + 1, cnt + len(copyFishLocs[nr][nc]), visit)
                visit.pop()
            # 방문 한 곳이면 깊이만 추가 후 이동.
            else:
                moveShark(nr, nc, dep + 1, cnt, visit)

from copy import deepcopy
if __name__ == "__main__":
    # 0,  1, 2, 3, 4,  5,  6, 7
    # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
    ddr = [0, -1, -1, -1, 0, 1, 1, 1]
    ddc = [-1, -1, 0, 1, 1, 1, 0, -1]    

    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    M, S = map(int, input().split())
    fish = [list(map(int, input().split())) for _ in range(M)]
    fishLocs = [[[] for _ in range(5)] for _ in range(5)]

    for r, c, d in fish:
        fishLocs[r][c].append(d-1)

    sr, sc = map(int, input().split())

    fishSmell = [[0] * 5 for _ in range(5)]

    for s in range(1, S+1):
        # 물고기 복제.
        # print("shakr", sr, sc)
        copyFishLocs = deepcopy(fishLocs)
        # print("initial fish", s)
        # for row in copyFishLocs[1:]: print(*row[1:])

        # 물고기 이동.
        copyFishLocs = moveFish()
        # print("move fish", s)
        # for row in copyFishLocs[1:]: print(*row[1:])
        # print("fish smell", s)
        # for row in fishSmell[1:]: print(*row[1:])

        # print()
        # 상어 이동.
        eaten = []
        maximum = -1e9 
        moveShark(sr, sc, 0, 0, [])
        # 상어 이동 후 물고기 제거.
        # print("eaten", eaten)
        # print()
        for r, c in eaten:
            if copyFishLocs[r][c]:
                copyFishLocs[r][c] = []
                fishSmell[r][c] = 3
        
        # 물고기 냄새 제거.
        for r in range(1, 5):
            for c in range(1, 5):
                if fishSmell[r][c] > 0:
                    fishSmell[r][c] -= 1

        # 물고기 복제.
        for r in range(1, 5):
            for c in range(1, 5):
                fishLocs[r][c] += copyFishLocs[r][c]
        
        # print("final", s)
        # for row in copyFishLocs[1:]: print(*row[1:])
        # print()

    answers = 0
    for r in range(1, 5):
        for c in range(1, 5):
            answers += len(fishLocs[r][c])

    print(answers)

