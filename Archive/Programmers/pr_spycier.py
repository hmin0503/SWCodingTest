import heapq
def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while True :
        milder = heapq.heappop(scoville)
        if milder >= K:
            return answer
        if len(scoville) < 1:
            return -1
        mild = heapq.heappop(scoville)
        mixed = milder + mild * 2
        heapq.heappush(scoville, mixed)
        answer += 1

    return answer
