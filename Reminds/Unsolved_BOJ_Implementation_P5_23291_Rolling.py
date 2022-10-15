#------------------------
# #Implementation #Simulation #Split #Rotate #Efficiency #pypy3 
# https://www.acmicpc.net/problem/23291
#------------------------

# 어항 일렬로. 한 마리 이상

# 물고기 수가 가장 적은 어항에 물고기 한 마리.
    # 여러 개라면 모두 한마리씩

# 어항 쌓기
    # 가장 왼쪽에 있는 어항을 그 옆에 올림

# 두개 이상 쌓인 어항을 공중부양 시켜서 시계방향 90도 회전.
    # 더 이상 쌓을 수 없을 때까지 반복

# 인접한 두 어항 끼리 물고기 교환.
    # 인접한 두 어항의 물고기 차이를 5로 나눈 몫이 0 이상이면 물고기 많은 쪽에서 적은 쪽으로 d 만큼 이동.
    # 기존 어항과 새로운 어항

# 어항 다시 원래대로 돌려놓기.

# 왼쪽 절반 공중부양 후 시계방향 90도 회전 2번 반복.

# 인접한 두 어항 끼리 물고기 교환.
    # 인접한 두 어항의 물고기 차이를 5로 나눈 몫이 0 이상이면 물고기 많은 쪽에서 적은 쪽으로 d 만큼 이동.
    # 기존 어항과 새로운 어항

# 어항 다시 원래대로 돌려놓기.

N, K = map(int, input().split())
bowl = list(map(int, input().split()))

# 물고기 수 적은 어항에 물고기 넣기
minimum = min(bowl)
for i in range(N):
    if bowl[i] == minimum:
        bowl[i] += 1

# 가장 왼쪽 어항 쌓기
idx = list(range(N))
tmp = [[-1]*N for _ in range(N)]
tmp[-1] = idx
tmp[-2][1] = tmp[-1][0]
tmp[-1][0] = -1
gravity = []
for c in range(N):
    cnt = 0
    if tmp[-1][c] != -1:
        cnt += 1
        for r in range(N-2,-1,-1):
            if tmp[r][c] != -1:
                cnt += 1
    if cnt > 1:
        gravity.append((N-1, c, cnt))
    else:
        break




# while True:
    

    
