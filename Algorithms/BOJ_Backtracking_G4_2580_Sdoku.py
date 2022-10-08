#------------------------
# #Backtracking #pypy3
# https://www.acmicpc.net/problem/2580
#------------------------
def checkBlock(r, c, n):
    mr = ((r//3)+1)*3
    mc = ((c//3)+1)*3
    for br in range(mr-3, mr):
        for bc in range(mc-3, mc):
            if n == sdoku[br][bc]:
                return False
    return True

def checkRow(r, n):
    if n in sdoku[r]:
        return False
    return True

def checkColumn(c, n):
    for r in range(9):
        if n == sdoku[r][c]:
            return False
    return True

def dfs(idx):
    if idx == len(empty):
        for i in range(9):
            print(*sdoku[i])
        exit(0)
        # return
    # 틀린 이유 1: 범위 주의 0~9가 아닌 1~10.
    # 틀린 이유 2: 모든 인덱스를 한번씩 돌면서 0인지 아닌지 판별할 필요 X !!. -> 너무 느려.
    # 빈 공간에 대한 인덱스를 이용하면 됨.
    # 틀린 이유 3: 값이 할당되지 않는 칸이 존재. 
    # -> empty를 잘못 관리한 듯? empty의 내용을 건들이지 마라. -> Why..?
    r, c = empty[idx]
    for n in range(1, 10):
        if checkRow(r, n) and checkColumn(c, n) and checkBlock(r, c, n):
            sdoku[r][c] = n
            dfs(idx+1)
            sdoku[r][c] = 0

if __name__ == '__main__':
    sdoku = [list(map(int, input().split())) for _ in range(9)]
    numbers = [0]*10
    empty = []
    for r in range(9):
        for c in range(9):
            if sdoku[r][c] == 0:
                empty.append((r,c))
    dfs(0)