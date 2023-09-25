import sys
input = sys.stdin.readline

def solution(N, schedule):
    [schedule_t, schedule_p] = schedule
    dp = [0] * (N+1) # 스케쥴 진행에 따른 i 번째 날의 최대 수익 기록하기

    # 마지막 날짜부터 거꾸로 계산하기
    for i in range(N-1, -1, -1):
        # i 번째 날에 상담을 하면 퇴사일을 넘기지 않을 경우,
        if schedule_t[i] + i <= N:
            # i 번째 날 상담을 진행하는 것과 하지 않는 경우 수익을 비교했을 때 비교
            dp[i] = max(dp[i+1], schedule_p[i] + dp[i + schedule_t[i]])
        # i 번째 날에 상담을 하면 퇴사일을 넘길 경우 상담 X
        else:
            # 상담을 하지 않으니 i+1 번째 날의 수익을 그대로 기록
            dp[i] = dp[i+1]
    return dp[0]

if __name__ == '__main__':
    # 날짜에 대한 인풋 받기
    N = int(input())

    # 스케쥴에 대한 인풋 데이터 받기
    schedule_t = []
    schedule_p = []
    for _ in range(N):
        t, p = map(int, input().split())
        schedule_t.append(t)
        schedule_p.append(p)

    print(solution(N, [schedule_t, schedule_p]))