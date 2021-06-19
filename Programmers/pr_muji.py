# 효율성을 완전히 무시했을 때는 단순 queue를 이용해서 풀 수 있었다.
# K 시간이 흐르는 경우를 따지는 것도 너무 오래 걸리는 걸까? 음식 개수를 이용해서 남는 음식을 찾아야 하려나.
from collections import deque

def solution(food_times, k):
    queue = deque([(k, v) for k, v in enumerate(food_times)])
    for _ in range(k):
        if len(queue) == 0:
            return -1
        k, v = queue.popleft()
        v -= 1
        if v != 0 :
            queue.append((k, v))
    if len(queue) == 0:
        return -1            
    else :
        k, v = queue.popleft()
        return k + 1
