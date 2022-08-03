#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Set #Map #Hash
# https://www.acmicpc.net/problem/1764
#------------------------

def main():
    N, M  = map(int, input().split())
    neverHeard = set([input() for _ in range(N)])
    neverSaw = set([input() for _ in range(M)])
    inter = neverHeard.intersection(neverSaw)
    inter = sorted(inter)
    print(len(inter))
    for s in inter:
        print(s)

if __name__ == '__main__':
    main()
    
    