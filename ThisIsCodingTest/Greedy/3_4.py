"""
1이 될 때까지
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
"""
#%%
n, k = map(int, input().split())

count = 0

while True:
    if n < k :
        break
    if n % k != 0:
        count += n % k
        n -= n % k
    n /= k
    count += 1

count += n - 1
print(count)
# %%
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k)*k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k
result += (n-1)
print(result)