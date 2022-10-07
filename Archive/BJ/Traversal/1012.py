#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Graph #Traversal #Stack #DFS
# https://www.acmicpc.net/problem/1012
#------------------------
import sys
sys.setrecursionlimit(10**9)
def dfs(maps, r, c):
    # 밭은 직사각형이다.
    if c <= -1 or c >= len(maps[0]) or r <= -1 or r >= len(maps):
        return False
    
    if maps[r][c] == 1:
        maps[r][c] = 0
        dfs(maps, r-1, c) # 상
        dfs(maps, r, c-1) # 좌
        dfs(maps, r+1, c) # 하
        dfs(maps, r, c+1) # 우
        return True
    return False

def main():
    T = int(input())
    for test_case in range(T):
        M, N, K = map(int, input().split())
        maps = [[0]*M for _ in range(N)]
        
        for _ in range(K):
            c, r = map(int, input().split())
            maps[r][c] = 1
        results = 0
        for r in range(N):
            for c in range(M):
                if dfs(maps, r, c) == True:
                    results += 1
        print(results)

if __name__ == '__main__':
    main()