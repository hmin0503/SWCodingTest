#------------------------
# #DataStructure #BinarySearch #Hash #Sort #SetMap
# https://www.acmicpc.net/problem/10816
#------------------------

from collections import Counter
if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    nums = Counter(nums)
    M = int(input())
    cand = list(map(int, input().split()))

    for c in cand:
        if c in nums:
            print(nums[c], end = " ")
        else:
            print(0, end = " ")
            
