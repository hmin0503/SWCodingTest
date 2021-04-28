"""
Q. 정수 삼각형

dp[i][j] = dp[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])
"""
#%%
n = int(input())

# dp 테이블 초기화
dp = []
for i in range(n):
    dp.append(list(map(int,input().split())))

# 점화식 코딩
for i in range(1, n):
    for j in range(i + 1):        
        # 가장 왼쪽은 왼쪽 위에서 내려오는 경우 x
        if j == 0 :
            up_left = 0
        else :
            up_left = dp[i - 1][j - 1]
        
        # 가장 오른쪽은 위에서 내려오는 경우 x
        if j == i :
            up = 0
        else :
            up = dp[i - 1][j]

        dp[i][j] = dp[i][j] + max(up_left, up)

# 가장 마지막 줄에서 max 값 보여주기
print(max(dp[i]))
# %%
