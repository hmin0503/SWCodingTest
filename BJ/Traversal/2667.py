#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Graph #Traversal #Stack #DFS
# https://www.acmicpc.net/problem/2667
# BFS로도 풀이 가능
#------------------------
import sys
sys.setrecursionlimit(10**9)
def dfs(maps, r, c):
    global cnt
    if c <= -1 or c >= len(maps) or r <= -1 or r >= len(maps):
        return False
    
    if maps[r][c] == 1:
        cnt += 1
        maps[r][c] = 0
        dfs(maps, r-1, c) # 상
        dfs(maps, r, c-1) # 좌
        dfs(maps, r+1, c) # 하
        dfs(maps, r, c+1) # 우
        return True
    return False

def main():
    global cnt
    N = int(input())
    maps = [list(map(int, list(input()))) for _ in range(N)]
    result = 0
    cnt = 0
    answers = []
    for r in range(N):
        for c in range(N):
            if dfs(maps, r, c) == True :
                answers.append(cnt)
                result += 1
                cnt = 0 
    print(result)
    print(*sorted(answers), sep = "\n") #오름차순 정렬 후 출력!!!

    
    

if __name__ == '__main__':
    main()