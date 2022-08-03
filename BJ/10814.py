#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Sort
# https://www.acmicpc.net/problem/10814
#------------------------

def solution():
    N = int(input())
    words = [[list(input().split()), i] for i in range(N)]
    words = list(sorted(words, key = lambda x: (int(x[0][0]),x[1])))
    print(words)
    for w, n in words:
        print(w[0], w[1])
        
if __name__ == '__main__':
    solution()