#------------------------
# 컨베이어 벨트 위의 로봇
# #Gold5 #Simulation #Implementation #Queue
# https://www.acmicpc.net/problem/20055
#------------------------

if __name__ == '__main__':
    N, K = map(int, input().split())
    conveyor = list(map(int, input().split()))
    loc = [0] * N
    step = 0
    while True:
        # print("start", loc, end = "->")

        # 1. 컨베이어 벨트 회전.
        loc = [0] + loc[:-1]
        conveyor = [conveyor[-1]] + conveyor[:-1]
        # print("rotate", loc, end = "->")
        
        # 1.1 N번째 로봇 하차.
        loc[-1] = 0

        # 2. 로봇이 스스로 이동.
        # 움직인 로봇의 위치를 새롭게 기록한다면 제대로 작동하지 않음. Why..? 
        # 다음 칸에 있는지 없는지를 확인하는 과정에서 문제가 생긴걸까?
        for i in range(len(loc)-2, -1, -1):
            if loc[i] == 1 and loc[i+1] == 0 and conveyor[i+1] > 0 :
                loc[i+1] = 1
                loc[i] = 0
                conveyor[i+1] -= 1
            else:
                continue
        # 2.1 N번째 로봇 하차.
        loc[-1] = 0 
        # print("robot move", loc, end = "->")
        # 3. 컨베이어 벨트 첫번째 칸에 로봇 올리기.

        if loc[0] == 0 and conveyor[0] > 0:
            loc[0] = 1
            conveyor[0] -= 1
            # print("load robot", loc, end = "->")
            
        
        step += 1

        # 4. 내구도가 0인 칸의 개수.
        # print("check durability", conveyor)
        if conveyor.count(0) >= K :
            print(step)
            break
        # for d in conveyor:
        #     if d == 0:
        #         cnt += 1
        # if cnt >= K :
        #     print(step)
        #     break
        
        
