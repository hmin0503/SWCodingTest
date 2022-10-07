#------------------------
# 톱니바퀴
# #Gold5 #Simulation #Implementation
# https://www.acmicpc.net/problem/14891
#------------------------
def rotate(gear, d):
    if d == 1:
        gear = [gear[-1]] + gear[:-1]
    else:
        gear = gear[1:] + [gear[0]]
    return gear

def propagation(n, d):
    r = [0]*4
    r[n-1] = d
    # forward-propagation
    i = 1
    for idx in range(n-1, 3):
        # print("forward", idx, end=": ")
        if G[idx][2] != G[idx+1][6]:
            # print(G[idx][2], G[idx+1][6])
            r[idx+1] = d*((-1)**i)
        else:
            break
        i += 1

    # back-propagation
    i = 1
    for idx in range(n-1, 0, -1):
        # print("back", idx)
        if G[idx][6] != G[idx-1][2]:
            r[idx-1] = d*((-1)**i)
        else:
            break
        i += 1
    return r

if __name__ == '__main__':
    # N: 0, S: 1
    G = [list(input()) for _ in range(4)]
    K = int(input())

    for _ in range(K):
        # n: num of a gear, d: direction -> 1: clock-wise, -1: counter-clock-wise
        n, d = map(int,input().split())
        r = propagation(n, d)
        # print(r)
    
        for i in range(4):
            if r[i] != 0:
                G[i] = rotate(G[i], r[i])
    
    print(int(G[0][0])*1 + int(G[1][0])*2 + int(G[2][0])*4 + int(G[3][0])*8)                        