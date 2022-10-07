#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Sort
# https://www.acmicpc.net/problem/2751
#------------------------

def solution():
    N = int(input())
    lst = [ 0 for _ in range(1000001)]
    for _ in range(N):
        lst[int(input())] += 1
    for i in range(1000001):
        for _ in range(lst[i]):
            print(i)

def solution_inner():
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    nums = sorted(nums)
    for n in nums:
        print(n)

def solution_sys():
    import sys
    N = int(input())
    nums = []
    for i in range(N):
        nums.append(int(sys.stdin.readline()))
    for i in sorted(nums):
        sys.stdout.write(str(i)+'\n')
if __name__ == '__main__':
    solution_sys()