"""
숫자 카드 게임
여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
"""
#%%
n, m = map(int, input().split())
minimum = []

for _ in range(n):
    rows = list(map(int, input().split()))
    minimum.append(min(rows))

print(max(minimum))
# %%
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(restul, min_value)

print(result)