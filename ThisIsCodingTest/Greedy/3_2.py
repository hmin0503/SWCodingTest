"""
큰 수의 법칙
주어진 수들을 M번 더하여 가장 큰 수를 만다는 법칙.
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번 초과하여 더해질 수 없는 것이 이 법칙의 특징
"""
#%%
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

result = first * (m - (m % k))
result += second * (m % k)

print(result)

# %%
