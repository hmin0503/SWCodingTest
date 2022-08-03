#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Set #Map #Hash
# https://www.acmicpc.net/problem/10816
#------------------------

def main():
    N = int(input())
    numList = [0] * 10000001*2
    for n in list(map(int, input().split())):
        numList[n + 10000000] += 1
    
    M = int(input())
    for n in (map(int, input().split())):
        print(numList[n + 10000000], end = " ")

def main():
    N = int(input())
    numList = {}
    for n in list(map(int, input().split())):
        if n in numList:
            numList[n] += 1
        else:
            numList[n] = 1
            
    M = int(input())
    for n in (map(int, input().split())):
        if n in numList:
            print(numList[n], end = " ") 
        else:
            print(0, end = " ")
if __name__ == '__main__':
    main()