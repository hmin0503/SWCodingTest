#------------------------
# 스타트와 링크
# #Silver2 #Backtracking #BruteForce
# https://www.acmicpc.net/problem/14889
#------------------------

def backtracking(groups, st, N):
    global minimum
    if len(groups) == N//2:
        groups = set(groups)
        starter, link = 0, 0
        for i in range(N):
            for j in range(i+1, N):
                if i in groups and j in groups:
                    starter += S[i][j]
                    starter += S[j][i]
                elif i not in groups and j not in groups:
                    link += S[i][j]
                    link += S[j][i]        
        # for i in groups:
        #     for j in groups:
        #         starter += S[i][j]
        # groups2 = set(range(1,N)).difference(groups)
        # for i in groups2:
        #     for j in groups2:
        #         link += S[i][j]
        minimum = min(abs(starter-link), minimum)
        return 
    for g in range(st, N):
        if g not in groups:
            groups.append(g)
            backtracking(groups, g+1, N)
            groups.pop()

if __name__ == '__main__':
    minimum = 1e9
    N = int(input())
    S = [list(map(int,input().split())) for _ in range(N)]
    backtracking([], 0, N)
    print(minimum)
