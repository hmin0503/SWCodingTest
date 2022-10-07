def solution(n):
    answer = 0
    reversed = ''
    while n >= 1:
        rest = n % 3
        reversed += str(rest)
        n //= 3
            
    for i in range(len(reversed)):
        answer += pow(3,i) * int(reversed[len(reversed) - i - 1])
    
    return answer