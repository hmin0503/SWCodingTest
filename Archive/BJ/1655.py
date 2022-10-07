#------------------------
# #우선순위큐 #자료구조
#------------------------
#%%
# 들어올때마다 출력해주면 시간 초과
def main():
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(int(input()))
        numbers.sort()
        l = len(numbers) + 1
        print(numbers[min(l//2, l/2)-1])
# %%
if __name__ == '__main__':
    main()
# %%
import heapq
def main():
    maxQ, minQ = [], []
    N = int(input())
    for i in range(N):
        n = int(input())
        if i%2 == 0:
            heapq.heappush(maxQ, n*-1)
        else:
            heapq.heappush(minQ, n)
        if maxQ and minQ and maxQ[0]*-1 > minQ[0]:
            temp = heapq.heappop(maxQ)*-1
            heapq.heappush(maxQ, heapq.heappop(minQ)*-1)
            heapq.heappush(minQ, temp)
        print(maxQ[0]*-1)
# %%
if __name__ == '__main__':
    main()

# %%