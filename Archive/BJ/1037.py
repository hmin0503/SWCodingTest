#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Math
# https://www.acmicpc.net/problem/1037
#------------------------

def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    return min(nums)*max(nums)

if __name__ == '__main__':
    print(solution())
    