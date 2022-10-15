# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에,
# 가장 긴 증가하는 부분 수열은 A = {'10', '20', 10, '30', 20, '50'} 이고, 길이는 4이다.

# DP 풀이법
if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    dp = [1]*N
    for i in range(N):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))

# Binary search 풀이법
import bisect
if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    dp = [A[0]]
    for i in range(N):
        if A[i] > dp[-1]:
            dp.append(A[i])
        else:
            idx = bisect.bisect_left(dp, A[i])
            dp[idx] = A[i]
    print(len(dp))

# # Binary search 풀이법 + 수열 찾기
# 14002번 
x = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_dp = max(dp)
print(max_dp)

max_idx = dp.index(max_dp)
lis = []

while max_idx >= 0:
    if dp[max_idx] == max_dp:
        lis.append(arr[max_idx])
        max_dp -= 1
    max_idx -= 1

lis.reverse()
print(*lis)