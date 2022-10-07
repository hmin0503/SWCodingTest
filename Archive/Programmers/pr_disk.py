import heapq
import math

def solution(jobs):
    answer = 0
    now = 0
    prev = -1
    loaded = []
    finished = 0
    
    while finished < len(jobs):
        for t, w in jobs:
            if prev < t <= now:
                heapq.heappush(loaded, [w,t])
        if loaded:
            w, t = heapq.heappop(loaded)
            prev = now
            now += w
            answer += now - t
            finished += 1
        else :
            now += 1
    return math.floor(answer / len(jobs))
            
