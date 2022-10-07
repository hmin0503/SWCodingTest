#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #PriorityQueue #절대값힙
# https://www.acmicpc.net/problem/11286
#------------------------
# def BinarySearch(numList, num):
#     st = 0
#     ed = len(numList)-1
#     while st <= ed:
#         mid = (st+ed)//2
#         if numList[mid] == num:
#             return 1
#         elif numList[mid] > num:
#             ed = mid - 1
#             # 왼쪽 노드로 접근: ed를 mid보다 작게
#         else:
#             st = mid + 1
#             # 오른쪽 노드로 접근: st를 mid보다 크게
#     return 0
   
def main():
    import sys, heapq
    N = int(input())
    nums = []
    for _ in range(N):
        idxInsert = 0
        n = int(sys.stdin.readline())
        if n == 0:
            if len(nums) == 0:
                sys.stdout.write(str(0)+"\n")
            else:
                sys.stdout.write(str(heapq.heappop(nums)[1])+"\n")
        else:
            heapq.heappush(nums, (abs(n), n))
if __name__ == '__main__':
    main()
    