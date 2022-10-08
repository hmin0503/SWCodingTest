#------------------------
# #PriorityQueue #Heap #DataStructure
# https://www.acmicpc.net/problem/11286
#------------------------

import heapq, sys
def main():
    N = int(input())
    # 최대힙, 최소힙 이용 방법 외에, 우선순위 값을 2개 두는 방법도 있음.
    maxH = [] # 음수 저장.
    minH = [] # 양수 저장.
    for _ in range(N):
        num = int(sys.stdin.readline())
        if num == 0:
            if len(minH) == 0 and len(maxH) == 0:
                print(0)
                continue
            elif len(minH) == 0:
                print(-heapq.heappop(maxH))
            elif len(maxH) == 0:
                print(heapq.heappop(minH))
            else:
                if maxH[0] == minH[0]:
                    print(-heapq.heappop(maxH))
                elif maxH[0] > minH[0]:
                    print(heapq.heappop(minH))
                elif maxH[0] < minH[0]:
                    print(-heapq.heappop(maxH))
        else:
            if num > 0:
                heapq.heappush(minH, num)
            elif num < 0:
                heapq.heappush(maxH, -num)
if __name__ == '__main__':
    main()