#------------------------
# 컨베이어 벨트 위의 로봇
# #Gold5 #Simulation #Implementation
# https://www.acmicpc.net/problem/20055
#------------------------

if __name__ == '__main__':
    N, K = map(int, input().split())
    conveyor = list(map(int, input().split()))
    loc = [0] * N
    step = 1
    while True:
        # 1. 컨베이어 벨트 회전.
        print("rotate", end = "->")
        loc = [loc[-1]] + loc[:-1]
        conveyor = [conveyor[-1]] + conveyor[:-1]

        # 2. 컨베이어 벨트 이동.
        newloc = [0] * N
        # 2.1. 로봇이 스스로 이동.
        print("robot move", end = "->")
        for i in range(len(loc)-2, -1, -1):
            if loc[i] == 1 and newloc[i+1] == 0 and conveyor[i+1] > 0 :
                newloc[i+1] = 1
                conveyor[i+1] -= 1
            else:
                continue
        loc = newloc
        # 3. 컨베이어 벨트 첫번째 칸에 로봇 올리기.
        print("load robot", end = "->")
        loc[0] = 1
        conveyor[0] -= 1
        
        # 4. 내구도가 0인 칸의 개수.
        print("check durability", conveyor)
        cnt = 0
        for d in conveyor:
            if d == 0:
                cnt += 1
        if cnt >= K :
            print(step)
            break
        
        step += 1
        
