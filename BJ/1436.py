#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #BruteForce
# https://www.acmicpc.net/problem/1436
#------------------------

def solution():
    N = int(input())
    num = 665
    while True:
        if N == 0 :
            print(num)
            break
        else:
            num += 1
            if '666' in str(num):
                N -= 1

if __name__ == '__main__':
    solution()