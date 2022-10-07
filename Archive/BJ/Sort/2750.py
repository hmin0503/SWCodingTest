#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Sort
# https://www.acmicpc.net/problem/2750
#------------------------

def solution():
    N = int(input())
    nums = [ int(input()) for _ in range(N)]
    nums = sorted(nums)
    for n in nums:
        print(n)

        
if __name__ == '__main__':
    solution()