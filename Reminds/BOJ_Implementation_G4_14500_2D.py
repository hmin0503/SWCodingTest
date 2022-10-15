#------------------------
# #Implementation #Simulation #BruteForce #Efficiency... #pypy3
# https://www.acmicpc.net/problem/14500
#------------------------
# 종이 위에 테트로미노 하나를 놓기
    # 한 점을 기준으로 놓기
    # 회전 해보기
    # 대칭 해보기
# 값이 최대가 되는가?


def b1Score(sr, sc):
    global maximum
    ddd = [[1,1,1], [1,2,3], [2,2,1], [2,1,2]]
    for dd in ddd: 
        for i in range(4): # 시계방향 회전
            for f in range(2): # 상하 반전
                r, c = sr, sc
                answers = blocks[r][c]
                for d in dd:
                    # 상, 하 방향 바꿔주기.
                    nd = (d-i) % 4
                    if f == 1 and nd % 2 == 0:
                        nd = (nd + 2) % 4
                    nr, nc = r + dr[nd], c + dc[nd]
                    # 직사각형 범위 주의
                    if 0 <= nr < N and 0 <= nc < M:
                        answers += blocks[nr][nc]
                        r, c = nr, nc
                    else:
                        break
                else:
                    if maximum < answers:
                        maximum = answers
def b5Score(sr, sc):
    global maximum
    ddd = [[1],[1,1],[1,2]]
    for i in range(4):
        for f in range(2):
            answers = blocks[sr][sc]
            for dd in ddd:
                r, c = sr, sc
                for d in dd:
                    nd = (d-i) % 4
                    if f == 1 and nd % 2 == 0:
                        nd = (nd+2) % 4
                    nr, nc = r + dr[nd], c + dc[nd]
                    r, c = nr, nc
                if 0 <= nr < N and 0 <= nc < M:
                    answers += blocks[nr][nc]
                else:
                    break
            else:
                if maximum < answers:
                    maximum = answers

if __name__ == '__main__':
    maximum = -1e9
    # 상후하좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    N, M = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(M):
            b1Score(r,c)
            b5Score(r,c)
    print(maximum)