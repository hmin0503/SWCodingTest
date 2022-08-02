#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #BruteForce
# https://www.acmicpc.net/problem/1018
# 이해가 안된다.
#------------------------

def solution():
    answers = []
    M, N = map(int, input().split())
    maps = [list(input()) for _ in range(M)]
    for i in range(M-7):
        for j in range(N-7):
            w = 0
            b = 0
            for c in range(i, i + 8):
                for r in range(j, j+ 8):
                    if (c+r) % 2 == 0:
                        if maps[c][r] != "W":
                            w += 1
                        else:
                            b += 1
                    else:
                        if maps[c][r] != "B":
                            w += 1
                        else:
                            b += 1
            answers.append(min(w,b))
    print(min(answers))
                
if __name__ == '__main__':
    solution()