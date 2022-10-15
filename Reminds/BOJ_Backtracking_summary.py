# https://www.acmicpc.net/problem/15649
# N와 M (1): 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
"""
Input: 
4 2
Output:
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
"""
def dfs(stack, N, M):
    if len(stack) == M:
        print(*stack)
        return
    for s in range(1, N+1):
        if s not in stack:
            stack.append(s)
            dfs(stack, N, M)
            stack.pop()
if __name__ == '__main__':
    N, M = map(int, input().split())
    stack = []
    dfs(stack, N, M)

# https://www.acmicpc.net/problem/15650
# N와 M (2): 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
"""
Input: 
4 2
Output:
1 2
1 3
1 4
2 3
2 4
3 4
"""
def dfs(stack, N, M, st):
    if len(stack) == M:
        print(*stack)
        return
    for s in range(st, N+1):
        if s not in stack:
            stack.append(s)
            dfs(stack, N, M, s+1)
            stack.pop()
if __name__ == '__main__':
    N, M = map(int, input().split())
    stack = []
    dfs(stack, N, M, 1)

# https://www.acmicpc.net/problem/15651
# N와 M(3): 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
"""
Input: 
4 2
Output:
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4
"""
def dfs(stack, N, M, st):
    if len(stack) == M:
        print(*stack)
        return
    for s in range(1, N+1):
        stack.append(s)
        dfs(stack, N, M, s+1)
        stack.pop()
if __name__ == '__main__':
    N, M = map(int, input().split())
    stack = []
    dfs(stack, N, M, 1)

# https://www.acmicpc.net/problem/15652
# N과 M (4): 1부터 N까지 자연수 중에서 M개를 고른 수열. 
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
"""
Input: 
4 2
Output:
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
"""
# https://www.acmicpc.net/problem/14888
# 연산자 끼워넣기
def dfs(n, total, add, sub, mul, div):
    global maximum, minimum
    if n == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    # 연산자 하나씩 제거하면서 넣어보기. -> 4방향 탐색과 비슷.
    if add:
        dfs(n+1, total + nums[n], add -1, sub, mul, div)
    if sub:
        dfs(n+1, total - nums[n], add, sub -1, mul, div)
    if mul:
        dfs(n+1, total * nums[n], add, sub, mul - 1, div)
    if div:
        dfs(n+1, int(total / nums[n]), add, sub, mul, div - 1)    
    
if __name__ == '__main__':
    maximum = -1e9
    minimum = 1e9
    
    N = int(input())
    nums = list(map(int, input().split()))
    ops = list(map(int, input().split()))
    dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])
    
    print(maximum)
    print(minimum)
    