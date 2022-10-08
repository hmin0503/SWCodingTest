#------------------------
# #PriorityQueue #DataStructure #시간초과
# https://www.acmicpc.net/problem/9461
#------------------------

import heapq, sys
if __name__ == '__main__':
    N = int(input())
    maxH = [] #최대힙: 값이 클 수록 우선순위 높음. (순서대로 나열 했을 때 중앙값 기준 앞부분.)
    minH = [] #최소힙: 값이 작을 수록 우선순위 높음. (순서대로 나열 했을 때 중앙값 기준 뒷부분.)
    for _ in range(N):
        num = int(sys.stdin.readline()) #시간초과
        # maxH가 minH 보다 항상 값이 1 크도록 유지.
        if len(maxH) == len(minH):
            heapq.heappush(maxH, -num)
        else:
            heapq.heappush(minH, num)
        
        if len(minH) == 0:
            print(-maxH[0]) # 원소가 1개라면 maxheap에서 출력. 그리고 다음 턴으로 넘어가기.
            continue
        # maxH는 항상 minH보다 작아야 하므로 값 비교 후 교체하기.
        if -maxH[0] > minH[0]:
            maxnum = -heapq.heappop(maxH)
            minnum = heapq.heappop(minH)

            heapq.heappush(maxH, -minnum)
            heapq.heappush(minH, maxnum)
        print(-maxH[0])
        

