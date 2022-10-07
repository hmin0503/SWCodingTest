#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Sort
# https://www.acmicpc.net/problem/1427
#------------------------

def solution():
    N = list(input())
    N = sorted(N, reverse = True)
    print(int("".join(N)))
if __name__ == '__main__':
    solution()