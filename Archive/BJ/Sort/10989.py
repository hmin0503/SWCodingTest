#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Sort #Counting sort
# https://www.acmicpc.net/problem/10989
#------------------------

def solution():
    import sys
    N = int(input())
    nums = [0] * 10001
    for _ in range(N):
        nums[int(sys.stdin.readline())] += 1

    for i in range(len(nums)):
        if nums[i] != 0:
            for _ in range(nums[i]):
                sys.stdout.write(str(i) + "\n")
        
if __name__ == '__main__':
    solution()