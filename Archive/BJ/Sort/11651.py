#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Sort
# https://www.acmicpc.net/problem/11651
#------------------------

def solution():
    N = int(input())
    coord = [list(map(int,input().split())) for _ in range(N)]
    coord = sorted(coord, key = lambda x : (x[1], x[0]), reverse = False)
    for x, y in coord:
        print(x, y)

        
if __name__ == '__main__':
    solution()