#------------------------
# 퇴사
# #Silver3
# https://www.acmicpc.net/problem/14501
#------------------------

def solution(N, schedule):
    memo = [0] * (N+1)
    for i in range(N-1, -1, -1):
        if schedule[i][0] + i <= N:
            memo[i] = max(schedule[i][1] + memo[i + schedule[i][0]], memo[i+1])
        else:
            memo[i] = memo[i+1]
    return memo[0]

if __name__ == '__main__':
    N = int(input())
    schedule = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, schedule))
