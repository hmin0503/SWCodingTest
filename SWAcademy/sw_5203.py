https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

"""
5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임
"""

# Run and Triplet
T = int(input())
for test_case in range(1,T+1):
    N = list(map(int,input().split()))
    A = [0,0,0,0,0,0,0,0,0,0]
    B = A.copy()
    result = 0
    for n in range(0,len(N),2):
        A[N[n]] += 1
        B[N[n+1]] += 1
        for i in range(1,9):
            if max(A) >= 3 or (A[i-1] >= 1 and A[i] >= 1 and A[i+1] >= 1) :
                result = 1
                break
        if result > 0:
            break
        for i in range(1,9):
            if max(B) >= 3 or (B[i-1] >= 1 and B[i] >= 1 and B[i+1] >= 1) :
                result = 2
                break
        if result > 0 :
            break
    print("#%d %d" % (test_case,result))
