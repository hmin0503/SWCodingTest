'''
https://programmers.co.kr/learn/courses/30/lessons/60058
'''


def correcting(u)
def solution(p):
    answer = ''
    if len(p) == 0:
        return answer
    else :
        while True:
            if (p[:2] == "()") | (p[:2] == ")(") :
                u = p[:2]
                v = p[2:]
            elif (p[-2:] == "()") (p[-2:] == ")(") : 
                u = p[:-2]
                v = p[-2:]
            
            stack = p.pop(0)

        return answer