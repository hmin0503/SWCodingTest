'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWSNw5jKzwMDFAUr&categoryId=AWSNw5jKzwMDFAUr&categoryType=CODE
Date : 2020-07-20
Memo : EASY
'''

def outline1(word):
    l = len(word)
    for _ in range(l):
        print("..#.", end="")
    print(".")

def outline2(word):
    l = len(word)
    for _ in range(l*2):
        print(".#", end="")
    print(".")


T = int(input())
for test_case in range(T):
    word = input()
    outline1(word)
    outline2(word)
    for i in range(len(word)):
        print("#."+word[i]+".",end="")
    print("#")
    outline2(word)
    outline1(word)