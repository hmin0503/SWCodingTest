"""
Q33 퇴사
i일때의 최대이익 = i + i-n 까지의 이익? xxx
dp[i] = i번째 일 부터 마지막 날 까지 낼 수 있는 최대 이익
p: profit
t: duration
dp[i] = max(p[i] + dp[t[i] + 1], max_value) ??????

"""
#%%
n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int,input().split())))

# %%
dp
# %%
