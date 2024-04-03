import sys
input = sys.stdin.readline
k = 6 # 6개의 원소를 가지는 부분 집합 구하기

def dfs(V, st):
    if len(V) == k:
        print(*V)
        return
    for i in range(st, N): # 중복을 출력하지 않기 위해 탐색 시작 구간을 조정
        if nums[i] not in V:
            V.append(nums[i])
            dfs(V, i + 1)
            V.pop()

while True:
    line = list(map(int, input().strip().split()))
    if line[0] == 0: # 여러 테스트 케이스가 제공되고, 0이 나올 때 입력이 끝남
        break
    N = line[0]
    nums = line[1:]
    dfs([], 0)
    print() # 테스트 케이스 간에 한 줄 띄우기