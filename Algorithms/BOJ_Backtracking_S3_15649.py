#------------------------
# #Backtracking
# https://www.acmicpc.net/problem/15649
#------------------------
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

