#-----------------------------------------------
# 로봇 청소기 G5 
# https://www.acmicpc.net/problem/15686
#-----------------------------------------------
# 현재 위치 청소
# 현재 위치에서 현재 방향 기준 왼쪽방향(반시계방향)부터 탐색.
    # 왼쪽 방향에 청소하지 않은 곳이 있다면 그 방향으로 회전 후 이동. 
        # -> 청소 -> 다시 탐색
    # 청소 가능한 곳 찾을 때 까지 회전 반복.
    # 청소 할 곳이 없다면, 또는 벽인 경우,
        # 바라보는 방향 유지하며 뒤로 이동. -> 다시 탐색
        # 후진 하는 곳이 벽이라면(아무것도 할 수 없다면) 중지.
#-----------------------------------------------

# N x M 직사각형
# 동,서,남,북

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
vr, vc, vd = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]
rooms[vr][vc] = 0
answers = 0
while True:
    # 방 청소
    # print()
    # print("Start", vr, vc, vd,  end = "->")
    if rooms[vr][vc] == 0:
        rooms[vr][vc] = 2
        answers += 1
    # 방향 탐색
    for i in range(1, 5):
        # print("Explore", end = "->")
        nd = (vd-i)%4
        nr, nc = vr + dr[nd], vc + dc[nd]
        if 0 < nr < N-1 and 0 < nc < M-1:
            if rooms[nr][nc] == 0:
                vr, vc, vd = nr, nc, nd
                # print("break", end = "->")
                break
    else:
        # print("Back try", end = "->")
        nr, nc, nd = vr + dr[nd]*(-1), vc + dc[nd]*(-1), nd
        if 0 < nr < N-1 and 0 < nc < M-1:
            if rooms[nr][nc] != 1:
                # print("Back", end = "->")
                vr, vc, vd = nr, nc, nd
            else:
                # print("Stop", end = "->")
                break
        else:
            break
print(answers)
