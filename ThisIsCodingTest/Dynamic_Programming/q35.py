"""
Q35 못생긴 수
dp[i] = min(2의배수, 3의배수, 5의배수)
"""
#%%
n = int(input())

dp = [0] * 1001

dp[1] = 1
i2 = i3 = i5 = 1
next2 = 2
next3 = 3
next5 = 5

for i in range(2, n+1):
    dp[i] = min(next2, next3, next5)

    if dp[i] == next2:
        i2 += 1
        next2 = 2 * dp[i2]

    if dp[i] == next3:
        i3 += 1
        next3 = 3 * dp[i3]

    if dp[i] == next5:
        i5 += 1
        next5 = 5 * dp[i5]

print(dp[n])




# %%
