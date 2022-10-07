def solution(triangle):
    dp = triangle

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i][j] + dp[i-1][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i][j] + dp[i-1][j-1]
            else :
                dp[i][j] = dp[i][j] + max(dp[i-1][j-1],dp[i-1][j])
    answer = max(dp[-1])
    return answer