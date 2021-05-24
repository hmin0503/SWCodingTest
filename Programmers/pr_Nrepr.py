"""
Programmers - N으로 표현
"""

def solution(N, number):
    max_num = 8
    N = str(N)
    memory = [[] for _ in range(max_num + 1)]
    for i in range(1, max_num + 1):
        if i == 1:
            memory[i].append(N)
        else :
            for n in memory[i-1]:
                memory[i].append(n + N)
                memory[i].append(n + "+" + N)
                
                memory[i].append("(" + n + ")" + "//" + N)
                memory[i].append(n + "//" + N)
                memory[i].append(n + "-" + N)
                
                memory[i].append("(" + n + ")" + "*" + N)
                memory[i].append( n + "*" + N)
        
        memory[i] = list(set(memory[i]))
        for n in memory[i]:
            if eval(n) == number:
                return i
    return -1
    
 # 처음부터 계산을 하면서 값을 저장해 가니 빼먹는 경우의 수가 존재하여, 
 # 먼저 수식을 string으로 표현한 뒤에 eval 내장함수를 이용해서, 재 계산을 하여 값이 맞는지 확인하였다.
 # For 구문을 2번 돌린 다는 점에서 효율적이지 못하다.
 # 문제에서 괄호에 대한 규칙이 명확히 규정되어 있지 않아서, 새로운 테스트 케이스가 추가된다면 틀릴지도 모르겠다.
