import heapq # 최소 힙(heap)

def solution(operations):
    heap = []
    for operation in operations:
        a, b = operation.split()
        if a == "I":
            heapq.heappush(heap, int(b))
        elif a == "D":
            if len(heap) > 0:
                if int(b) == 1:
                	# 최소 힙 알고리즘에서 가장 큰 값을 제외하는 경우에 
                    # heapq의 nsmallest를 이용해 heap 내부의 값을 정렬하고 
                    # 가장 큰 값을 제외하고 다시 return 해준다. 
                    heap = heapq.nsmallest(len(heap), heap)[:-1]
                else :
                    heapq.heappop(heap)
    if  len(heap) == 0:
        return [0, 0]
    else :
    	# 값을 return 해주기 전에 정렬이 필요하다. ***
        heap = heapq.nsmallest(len(heap), heap)
        answer = [heap[-1], heap[0]]
        return answer
