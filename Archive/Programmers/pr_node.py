from collections import deque
def solution(n, edge):
    lengths = [0] * (n + 1)
    graphs = {i:[] for i in range(1, n + 1)}
    queue = deque()
    
    for i, j in edge:
        graphs[i].append(j)
        graphs[j].append(i)
    
    start = 1
    lengths[1] = 1
    queue.append(start)
    
    while queue:
        q = queue.popleft()
        for n in graphs[q]:
            if lengths[n] != 0:
                continue
            lengths[n] += lengths[q] + 1
            queue.append(n)
            
    answer = 0
    m = max(lengths)
    for l in lengths:
        if l == m:
            answer += 1
    return answer
