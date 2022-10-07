"""
왕실의 나이트
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
"""
#%%
loc = input()
row = int(loc[1:])
col = int(ord(loc[0]) - ord("a")) + 1
assert row <= 8 and col <= 8, "should be lower than 'h8'"

steps = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]
result = 0
for dx, dy in steps:
    next_row = row + dx
    next_col = col + dy
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)
# %%
