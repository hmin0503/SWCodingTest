#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #BruteForce
# https://www.acmicpc.net/problem/7568
#------------------------

def solution():
    N = int(input())
    orders = []
    users = []
    for i in range(N):
        x, y = map(int, input().split())
        users.append((x,y))
    # 모두 모든 사람과 한번 씩 다 비교
    for i in range(N):
        x = 1
        for j in range(N):
            # i 번째 사람이 j 번째보다 키와 몸무게가 모두 큰가?
            if (users[i][0] < users[j][0]) and (users[i][1] < users[j][1]):
                x += 1
        orders.append(x)
    print(*orders)
if __name__ == '__main__':
    solution()