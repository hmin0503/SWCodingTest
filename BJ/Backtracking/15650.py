#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #BackTracking #DFS #Silver3 
# https://www.acmicpc.net/problem/15650
#------------------------

def dfs(lst, st, N, M):
    if len(lst) == M:
        print(*lst)
        return

    for num in range(st, N+1):
        if num not in lst:
            # 넣어 주고 다시 탐색.
            lst.append(num)
            dfs(lst, num+1, N, M)
            # 다시 빼기
            lst.pop()
            
def main():
    N, M = map(int, input().split())
    lst = []
    dfs(lst, 1, N, M)

if __name__ == '__main__':
    main()