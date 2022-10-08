#------------------------
# #PriorityQueue #Heap #DataStructure
# https://www.acmicpc.net/problem/1927
#------------------------

import heapq, sys
def main():
    N = int(input())
    minH = []
    for _ in range(N):
        num = int(sys.stdin.readline())
        if num == 0:
            if len(minH) == 0:
                print(0)
                continue
            else:
                print(heapq.heappop(minH))
        else:
            heapq.heappush(minH, num)
if __name__ == '__main__':
    main()