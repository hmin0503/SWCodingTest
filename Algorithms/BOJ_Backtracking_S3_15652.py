#------------------------
# #Backtracking #Recursion
# https://www.acmicpc.net/problem/15652
#------------------------
def dfs(stack, N, M, st):
    if len(stack) == M:
        print(*stack)
        return
    for s in range(st, N+1):
        stack.append(s)
        dfs(stack, N, M, stack[-1])
        stack.pop()
if __name__ == '__main__':
    N, M = map(int, input().split())
    stack = []
    dfs(stack, N, M, 1)