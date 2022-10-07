#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Set #Map #Hash
# https://www.acmicpc.net/problem/1269
#------------------------

def main():
    N, M  = map(int, input().split())
    A = set(input().split())
    B = set(input().split())
    print(len(A - B) + len(B-A))

if __name__ == '__main__':
    main()