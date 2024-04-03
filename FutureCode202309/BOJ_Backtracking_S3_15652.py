import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def dfs(V, st):
    if len(V) == M: # 길이를 만족하면 수열 출력
        print(*V)
        return

    # 오름차순 수열을 구해야 하기 때문에 start 지정 필수
    for i in range(st, N+1): 
        V.append(i)
        dfs(V, i) # 같은 수를 여러 번 골라도 되기 때문에 "i"
        V.pop()
dfs([], 1)