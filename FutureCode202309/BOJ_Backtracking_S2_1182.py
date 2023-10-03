import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, S = map(int, input().split())
nums = list(map(int, input().split()))
visited = [0] * N
cnt = 0 
def dfs(V, st):
    global cnt
    if len(V) > 0 and sum([nums[idx] for idx in V]) == S: # 부분 집합 합이 S 라면 stop
        cnt += 1

    for i in range(st, N): # 겹치는 부분 집합이 없도록 앞에서부터 하나씩 탐색
        if i not in V:
            V.append(i)
            dfs(V, i+1)
            V.pop()

dfs([], 0)
print(cnt)

#------------------
# 비트 연산 활용
#------------------
import sys
input = sys.stdin.readline

n,s = map(int,input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(1<<n): # 부분 집합 개수를 구하여 모든 경우에 대해서 탐색
    tmp = 0
    for j in range(n):
        if i&(1<<j):
            tmp += arr[j]
    if tmp==s:
        ans+=1
print(ans)