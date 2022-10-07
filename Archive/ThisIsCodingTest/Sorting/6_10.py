"""
위에서 아래로 정렬
"""
#%%

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array = sorted(array, reverse = True)

for i in range(n):
    print(array[i], end=' ')
# %%
