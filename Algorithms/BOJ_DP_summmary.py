# 파도반 수열
# https://www.acmicpc.net/problem/9461

# 점화식: dp[i] = dp[i-1] + dp[i-5]
def triangle(n):
    for i in range(1, n+1):
        if i < 4:
            dp[i] = 1
        elif i == 4 or i == 5:
            dp[i] = 2
        else:
            dp[i] = dp[i-1] + dp[i-5]
    return dp[n]
if __name__ == '__main__':
    T = int(input())
    dp = [0] * (101)
    for _ in range(T):
        N = int(input())
        print(triangle(N))

# 다른 점화식: dp[i+3] = dp[i] + dp[i+1]
wh = [0 for i in range(101)]
wh[1] = 1
wh[2] = 1
wh[3] = 1
for i in range(0, 98):
    wh[i + 3] = wh[i] + wh[i + 1]
t = int(input())
for i in range(t):
    n = int(input())
    print(wh[n])

# https://www.acmicpc.net/problem/1463
# 1로 만들기
if __name__ == "__main__":
    N = int(input())
    # DP 이용하기!!
    d = [0 for _ in range(N+2)]
    for i in range(2, N + 1):
        d[i] = d[i-1] + 1
        if i % 3 == 0:
            d[i] = min(d[i], d[i//3] + 1)
        if i % 2 == 0:
            d[i] = min(d[i], d[i//2] + 1)
    print(d[N])

# https://www.acmicpc.net/problem/12865
# 평범한 배낭 (Hard)
if __name__ == '__main__':
    N, K = map(int, input().split())
    weights = []
    values = []
    for _ in range(N):
        w, v = map(int, input().split())
        weights.append(w)
        values.append(v)
    bag = [[0]*(K+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1,K+1):
            w, v = weights[i-1], values[i-1]
            
            if j < w:
                bag[i][j] = bag[i-1][j]
            else:
                bag[i][j] = max(bag[i-1][j], bag[i-1][j-w]+v)
    print(bag[N][K])