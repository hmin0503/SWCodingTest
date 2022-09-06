#------------------------
# 시험 감독
# #Bronze2
# https://www.acmicpc.net/problem/13458
#------------------------
import math

def solution(n, a, b, c):
    cnt = 0
    for x in a:
        if x > max(b, c):
            cnt += math.ceil((x-max(b, c))/c)
    return cnt

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b, c = map(int, input().split())
    print(solution(n, a, b, c))
