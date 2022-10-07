"""
음료수 얼려 먹기
TOO HARD
"""
#%%
n, m = map(int, input().split())

# 얼음 틀 형태 입력받기
array = []
for _ in range(n):
    array.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if array[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
# %%

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x, y):
    if x <= -1 or x >= n or y >= m or y <= -1:
        return False
    
    if graph[x][y] == 0 :
        graph[x][y] = 1
        dfs(x - 1,  y)
        dfs(x + 1 , y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
# %%
