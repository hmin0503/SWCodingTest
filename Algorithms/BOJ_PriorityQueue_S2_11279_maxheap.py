#------------------------
# #PriorityQueue #Heap #DataStructure
# https://www.acmicpc.net/problem/11279
#------------------------

import heapq, sys
def main():
    N = int(input())
    maxH = []
    for _ in range(N):
        num = int(sys.stdin.readline())
        if num == 0:
            if len(maxH) == 0:
                print(0)
                continue
            else:
                print(-heapq.heappop(maxH))
        else:
            heapq.heappush(maxH, -num)
if __name__ == '__main__':
    main()