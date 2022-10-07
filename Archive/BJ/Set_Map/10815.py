#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Set #Map #BinarySearch
# https://www.acmicpc.net/problem/10815
#------------------------
def BinarySearch(numList, num):
    st = 0
    ed = len(numList)-1
    while st <= ed:
        mid = (st+ed)//2
        if numList[mid] == num:
            return 1
        elif numList[mid] > num:
            ed = mid - 1
            # 왼쪽 노드로 접근: ed를 mid보다 작게
        else:
            st = mid + 1
            # 오른쪽 노드로 접근: st를 mid보다 크게
    return 0
   
def solution1():
    N = int(input())
    #list말고 set으로 하니 통과
    numList = set(map(int,input().split()))
    M = int(input())
    comp = list(map(int, input().split()))
    for i in range(M):
        if comp[i] in numList:
            print(1, end = " ")
        else:
            print(0, end = " ")
def solution2():
    N = int(input())
    #BinarySearch -> Sorting 필수
    numList = list(map(int,input().split()))
    numList = sorted(numList)
    M = int(input())
    comp = list(map(int, input().split()))
    
    for i in range(M):
        print(BinarySearch(numList, comp[i]), end = " ")
if __name__ == '__main__':
    solution2()
    