'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14P0c6AAUCFAYi&categoryId=AV14P0c6AAUCFAYi&categoryType=CODE
Date : 2020-07-08
MeMo : EASY
'''
#%%
T = 10
for _ in range(T):
    test_case = int(input())
    keyword = input()
    search = input()
    print("#%d %d" %(test_case,search.count(keyword)))
