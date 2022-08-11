#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Recursion #Silver1
# https://www.acmicpc.net/problem/11729
#------------------------
import sys
sys.setrecursionlimit(10**9)
    
    
def hanoi(st, ed, N):
    print("#",N,"#")
    if N == 1:
        print(st, ed)
        return
    hanoi(st, 6-st-ed, N-1) 
    print(st, ed)
    hanoi(6-st-ed, ed, N-1)

def main():
    N = int(input())
    print(2**N-1)
    hanoi(1,3,N)
    
    
if __name__ == '__main__':
    main()
