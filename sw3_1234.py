'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14_DEKAJcCFAYD&categoryId=AV14_DEKAJcCFAYD&categoryType=CODE
Date : 2020-07-08
MeMo : 어렵다 어려워
'''
#%%
from collections import Counter

T = 10
for test_case in range(1,T+1):
    n, numbers = input().split()
    while True :
        stop = 0
        for i in range(len(numbers)-1):
            try :
                if numbers[i]==numbers[(i+1)]:
                    stop += 1
                    numbers = numbers[:i] + numbers[(i+1):]
                    numbers = numbers[:i] + numbers[(i+1):]
            except IndexError:
                break
        if stop == 0:
            print("#%d %d" % (test_case,int(numbers)))
            break



        

# %%
