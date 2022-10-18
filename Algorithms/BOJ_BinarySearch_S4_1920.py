#------------------------
# #DataStructure #BinarySearch
# https://www.acmicpc.net/problem/1920
#------------------------

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    M = int(input())
    cand = list(map(int, input().split()))

    for c in cand:
        st, ed = 0, len(nums)-1
        while True:
            # 틀린 이유: st가 ed와 같을 때 값이 존재할 수도 있음.
            if st > ed:
                print(0)
                break
            mid = (st+ed)//2
            if c == nums[mid]:
                print(1)
                break
            elif c > nums[mid]:
                st = mid+1
            elif c < nums[mid]:
                ed = mid-1
            
