import sys
input = sys.stdin.readline

def dfs(V):
    if len(V) == M: # 수열의 길이가 조건을 만족하면 재귀 함수 멈춤
        print(*[nums[i] for i in V]) # 출력
        return
    for i in range(N): # 처음부터 하나씩 탐색 진행
        if i not in V: # 동일한 수열이 중복되지 않도록 확인
            V.append(i)
            dfs(V)
            V.pop()

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

dfs([])