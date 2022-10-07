#------------------------
# 상어 초등학교
# #Gold5 #Implementation
# https://www.acmicpc.net/problem/21608
#------------------------

def arrangement(orders, likes):
    # up, right, down, left
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    visited = [[0]*N for _ in range(N)]
    for s in orders:
        maps = {} #{(r,c):[0,0] for r in range(N) for c in range(N)}
        for r in range(N):
            for c in range(N):
                if visited[r][c] == 0:
                    maps[(r,c)] = [0, 0]
                    for i in range(4):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if 0 <= nr < N and 0 <= nc < N:
                            if visited[nr][nc] in likes[s]:
                                maps[(r,c)][0] += 1 # check contents
                            if visited[nr][nc] == 0:
                                maps[(r,c)][1] += 1 # check adj is empty
        maps = sorted(maps.items(), key = lambda x: (x[1][0], x[1][1], -x[0][0], -x[0][1]), reverse=True)
        r, c = maps[0][0]
        visited[r][c] = s
    return visited

def calculate(visited):

    # up, right, down, left
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    contents = 0
    N = len(visited)
    for r in range(N):
        for c in range(N):
            adj = 0
            s = visited[r][c]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    if visited[nr][nc] in likes[s]:
                        adj += 1
            if adj > 0:
                contents += 10**(adj-1)
    return contents

if __name__ == '__main__':
    N = int(input())
    likes = {}
    orders = []
    for _ in range(N**2):
        student = list(map(int, input().split()))
        likes[student[0]] = student[1:]
        orders.append(student[0])

    visited = arrangement(orders, likes)
    contents = calculate(visited)
    print(contents)