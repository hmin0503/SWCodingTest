#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Sort
# https://www.acmicpc.net/problem/1181
#------------------------

def solution():
    N = int(input())
    words = [input() for _ in range(N)]
    words = list(set(words))
    words = list(sorted(words, key = lambda x: (len(x),x)))
    for w in words:
        print(w)
    
        
if __name__ == '__main__':
    solution()