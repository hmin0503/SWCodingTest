#------------------------
# #DP #Silver2
# https://www.acmicpc.net/problem/9461
# 점화식 구하기!
#------------------------

def solution(nums):
    total = [nums[0]]
    for i in range(len(nums)-1):
        total.append(max(total[i]+nums[i+1], nums[i+1]))
    print(max(total))
if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    solution(nums)