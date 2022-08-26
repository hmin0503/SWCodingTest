#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Sort
# https://www.acmicpc.net/problem/18870
#------------------------
def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    nums_rep = list(sorted(set(nums)))
    # list.index()는 시간복잡도가 높음.
    # nums = [nums_rep.index(n) for n in nums]
    nums_rep = {nums_rep[i]:i for i in range(len(nums_rep))}
    for n in nums:
        print(nums_rep[n], end= " ")
    # print(*nums) #sperate arguments
if __name__ == '__main__':
    solution()
