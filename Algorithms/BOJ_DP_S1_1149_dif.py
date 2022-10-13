#------------------------
# #DP
# https://www.acmicpc.net/problem/1149
#------------------------

if __name__ == '__main__':
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    
    dpCost = [[0]*3 for _ in range(N)]
    dpCost[0] = cost[0]
    for idx in range(1, N):
        dpCost[idx][0] = min(dpCost[idx-1][1], dpCost[idx-1][2]) + cost[idx][0]
        dpCost[idx][1] = min(dpCost[idx-1][0], dpCost[idx-1][2]) + cost[idx][1]
        dpCost[idx][2] = min(dpCost[idx-1][0], dpCost[idx-1][1]) + cost[idx][2]
    print(min(dpCost[-1]))