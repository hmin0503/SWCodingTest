#------------------------
# #Backtracking #BruteForce #Recursion
# https://www.acmicpc.net/problem/9663
#------------------------
def checkDiag(stack):
    if len(stack) < 3:
        return True
    r, c = len(stack)-1, stack[-1]
    for nr in range(len(stack)-2, 0, -1):
        if abs(r - nr)/abs(c-stack[nr]) == 1:
            return False
    return True

def dfs(stack, N):
    global cnt
    if len(stack) == N+1:
        cnt += 1
        return
    for s in range(1, N+1):
        if s not in stack:
            stack.append(s)
            if checkDiag(stack):
                dfs(stack, N)
            stack.pop()

if __name__ == '__main__':
    N = int(input())
    cnt = 0
    stack = [0]
    dfs(stack, N)
    print(cnt)