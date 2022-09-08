#------------------------
# 로봇 청소기
# #Gold5 #Simulation #Implementation
# https://www.acmicpc.net/problem/14503
#------------------------

def cleaning(r, c, maps):
    maps[r][c] = 2
    return maps

def rotate(d):
    d_new = (d+3)%4
    return d_new

def move(r, c, d, forward = True):
    # 0: north, 1:east, 2: south, 3: west
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    if forward:
        r_new = r + dr[d]
        c_new = c + dc[d]
    else:
        r_new = r - dr[d]
        c_new = c - dc[d]
    return r_new, c_new

def left_check(r, c, d, maps):
    if 0 < r_new < N-1 and 0 < c_new < M-1 and maps[r_new][c_new] == 0:
        return True
    return False

if __name__ == '__main__':
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    maps[r][c] = 2
    cnt += 1
    # 0: north, 1:east, 2: south, 3: west
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    r_old, c_old, d_old = r, c, d

    while True:
        # 1. 청소하기
        if maps[r][c] == 0:
            maps = cleaning(r, c, maps)
            cnt += 1

        # 2.3. 모든 방향이 이미 청소가 되었거나, 벽인 경우(이동 없이 다시 기존 방향으로 돌아온 경우)  후진 하기.
        if d_old == d:
            r_new = r - dr[d]
            c_new = c - dc[d]
            
            if 0 < r_new < N-1 and 0 < c_new < M-1 and maps[r_new][c_new] != 1:
                r, c = r_new, c_new

            # 2.4. 뒤쪽 방향이 벽이라 후진을 할 수 없는 경우 작동 중지.
            else:
                break
        print("origin", r, c, d,  end = "->")
        d_new = rotate(d)
        r_new, c_new = move(r, c, d_new)
        # 2.1. 왼쪽 방향에 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터
        if left_check(r_new, c_new, d_new, maps):
            maps = cleaning(r_new, c_new, maps)
            cnt += 1
            r_old, c_old, d_old = r, c, d
            r, c, d = r_new, c_new, d_new
            print("new", r, c, d)
        # 2.2. 왼쪽 방향에 청소할 공간이 없다면(이미 청소를 했거나 벽이거나), 그 방향으로 회전한 다음 2.1로 돌아가기.
        else:
            d = d_new
    print()
    for lst in maps:
        print(*lst)
    print(cnt)