'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWNcD_66pUEDFAV8&categoryId=AWNcD_66pUEDFAV8&categoryType=CODE
Date : 2020-07-08
MeMo : Easy
'''
#%%
import re
T = int(input())
for test_case in range(1,T+1):
    words = input()
    print("#{} {}".format(test_case,''.join(re.findall("[^aeiou]",words))))
