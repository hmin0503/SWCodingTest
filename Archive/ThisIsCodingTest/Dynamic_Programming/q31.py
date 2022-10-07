"""
DP
금광
"""
#%%
T = int(input())

for i in range(T):
    n, m = input().split()
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])        
        index += m
    
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i - 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    
    print(result)

#%%
"""
Q31 금광
dp[i][j] = dp[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j + 1], dp[i - 1][j])
"""

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    dp =[]
    array = list(map(int, input().split()))
    for i in range(0,n*m, m):
        dp.append(array[i:(i+m)])

    for i in range(1, m):
        for j in range(n):
            
            # 왼쪽 위가 없는 경우
            if j == 0:
                up_left = 0
            else :
                up_left = dp[j - 1][i - 1]
            
            left = dp[j][i - 1]

            # 왼쪽 아래가 없는 경우
            if j == n - 1:
                down_left = 0
            else :
                down_left = dp[j + 1][i - 1]

            # 왼쪽, 왼쪽 위, 왼쪽 아래 중에서 가장 큰 값을 더해 줌.
            dp[j][i] = dp[j][i] + max(up_left, left, down_left)
    
    # 마지막 column에서 max_value를 찾아줌.
    result = 0
    for i in range(n):
        result = max(result, dp[i][-1])
    print(result)
# %%
