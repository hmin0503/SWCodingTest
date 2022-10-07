#------------------------
# #DP #Silver2 #pypy3
# https://www.acmicpc.net/problem/9184
# list와 dictionary 비슷하려나?
#------------------------

def w(a, b, c):

    # 값이 존재하면 바로 return
    if (a,b,c) in memo:
        return memo[(a,b,c)]
    
    # 음수가 있으면 무조건 1
    if a <= 0 or b <= 0 or c <= 0:
        memo[(a,b,c)] = 1
        return memo[(a,b,c)]
    
    # 20 이하로 제한
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    
    # 계산 값은 바로 저장하기
    if a < b and b < c:
        memo[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c) 
        return memo[(a,b,c)]
    memo[(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1) 
    return memo[(a,b,c)]

if __name__ == '__main__':
    import sys
    memo = {} # 인풋이 들어올 때 마다 계속 새로 갱신할 필요 없음
    while True:
        a, b, c = map(int, sys.stdin.readline().split())
        if a == -1 and b == -1 and c == -1:
            break
        print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
        