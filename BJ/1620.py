#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Set #Map #Hash
# https://www.acmicpc.net/problem/1620
#------------------------

import sys
def main():
    N, M = map(int, input().split())
    d = {input():i for i in range(N)}
    d_r = [k for k,v in d.items()]
    
    for _ in range(M):
        idx = sys.stdin.readline().rstrip()
        if idx.isnumeric():
            sys.stdout.write(str(d_r[int(idx)-1]))
        else:
            sys.stdout.write(str(d[idx]+1))

if __name__ == '__main__':
    main()