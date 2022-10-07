'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWNcD_66pUEDFAV8&categoryId=AWNcD_66pUEDFAV8&categoryType=CODE
Date : 2020-07-20
Memo : Easy,,문제의도를 알 수 없다.
'''

T = int(input())
for test_case in range(1,T+1):
    print("#%d" % (test_case),end=" ")
    N = int(input())
    for _ in range(1,N+1):
        print("1/"+str(N),end=" ")
    print()