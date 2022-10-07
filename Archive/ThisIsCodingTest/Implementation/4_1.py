"""
상하좌우

"""
#%%
n = int(input())
directions = map(str, input().split())
start = [1, 1]
direction_dict = {
    "L" : [0, -1],
    "R" : [0, +1],
    "U" : [-1, 0],
    "D" : [+1, 0]
}
for d in directions:
    steps = direction_dict[d]
    if (start[0] + steps[0] < 1) | (start[1] + steps[0] < 1) | (start[0] + steps[0] > n) | (start[0] + steps[0] > n):
        continue
    start[0] += steps[0]
    start[1] += steps[1]

print(start[0], start[1])
# %%
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
        
print(x, y)
# %%
