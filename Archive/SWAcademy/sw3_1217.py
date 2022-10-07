'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14dUIaAAUCFAYD&categoryId=AV14dUIaAAUCFAYD&categoryType=CODE
Date : 2020-07-08
MeMo : Easy
'''
#%%
T = 10
def pow(base, exponent):
    if exponent == 2:
        return base*base
    else :
        base *= pow(base,exponent-1)
        return base
for _ in range(1, T + 1):
    test_case = str(input())
    a, b = map(int,input().split())
    print("#"+test_case,pow(a,b))
