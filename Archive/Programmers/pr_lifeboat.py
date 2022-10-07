from collections import deque

def solution(people, limit):
    answer =0
    people.sort()
    people = deque(people)
    while people:
        person1 = people.pop()
        cap = person1
        d = 0
        for person2 in people:
            if cap + person2 <= limit:
                cap += person2
                d += 1
            else :
                break
        # 원래 for문 안에 넣어 줬는데, error 떠서 독립
        for _ in range(d):
            people.popleft()
            
        answer += 1
        
    return answer
