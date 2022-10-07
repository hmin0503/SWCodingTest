#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #PriorityQueue #가운데를말해요 #Gold2
# https://www.acmicpc.net/problem/1165
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
    # 최대힙의 루트와 최소힙의 루트를 비교할 때, 실제 값으로 비교하기 때문에 음수가 입력되어도 문제 x
    maxH = [] # 중앙값을 기준으로 작은 값을 저장 -> 최대힙으로 구현하여 루트가 가장 큰 값.
    minH = [] # 중앙값을 기준으로 큰 값을 저장 -> 최소힙으로 구현하여 루트가 가장 작은 값.
    for _ in range(N):
        n = int(sys.stdin.readline())
        # maxH의 크기는 minH와 같거나 1만큼 크게 유지.
        if len(maxH) == len(minH):
            heapq.heappush(maxH, -n)
        else:
            heapq.heappush(minH, n)
            
        if len(minH) == 0:
            print(-maxH[0]) # minH가 비었다는 것은 들어온 숫자가 1개라는 뜻이므로 maxH에서 값을 찾아서 프린트.
            continue

        if -maxH[0] > minH[0]: 
            # maxH에 minH 최솟값보다 큰 값이 들어 있다면 서로 바꾸어주어서 min_nums가 항상 작은 값을 유지하도록 함. 
            n = -heapq.heappop(maxH)
            m = heapq.heappop(minH)
            heapq.heappush(maxH, -m)
            heapq.heappush(minH, n)
        
        print(-maxH[0])
                

if __name__ == '__main__':
    main()
    