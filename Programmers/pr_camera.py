def solution(routes):
    answer = 0
    routes = sorted(routes, key = lambda x: x[0])
    
    answer = 1
    s, e = routes[0]
    for i in range(1, len(routes)):
        if routes[i][0] >= s and routes[i][0] <= e :
            s = max(s, routes[i][0])
            e = min(e, routes[i][1])
        else :
            answer += 1
            s, e = routes[i]
    return answer
