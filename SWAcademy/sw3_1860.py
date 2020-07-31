'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LsaaqDzYDFAXc&categoryId=AV5LsaaqDzYDFAXc&categoryType=CODE
Date : 2020-07-20
Memo : Intermediate
'''

T = int(input())
for test_case in range(1,T+1):
    print("#%d" % (test_case), end=" ")
    N, M, K = map(int,input().split())
    waiting_list = list(map(int,input().split()))
    waiting_list.sort()
    for i in range(N):
        if  (i+1) <= (waiting_list[i] // M) * K :
            result = "Possible"
        else:
            result = "Impossible"
            break
    print(result)