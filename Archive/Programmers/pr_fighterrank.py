def solution(n, results):
    answer = 0
    win = {k:set() for k in range(1, n + 1)}
    lose = {k:set() for k in range(1, n + 1)}
    for i, j in results :
        win[i].add(j)
        lose[j].add(i)
        
    for i in range(1, n + 1):
        for w in lose[i]:
            win[w].update(win[i])
        for l in win[i]:
            lose[l].update(lose[i])
    
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer
