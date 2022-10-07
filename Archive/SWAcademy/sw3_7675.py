# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWqPvqoqSLQDFAT_&categoryId=AWqPvqoqSLQDFAT_&categoryType=CODE

'''
Date : 2020-07-08
Memo : 숫자만 어떻게 빼내지...
Input : 
2  // 테스트 케이스 개수
2  // 첫 번째 테스트 케이스, N = 2
Annyung Hasae Yo! LoL!
3
my name is Hye Soo. my id is   // 두 번째 테스트 케이스, N = 3
Rhs0266. what your id Bro?	
'''
#%%
import re

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    sentence = str(input())
    sentences = re.split("[!.?]",sentence)
    print("#"+str(test_case)+" ", end="")
    for i in range(N):
        words = re.findall(r"\b[A-Z][a-z]*[A-Z]{0}\b",sentences[i])
        print(len(words) - len(re.findall(r"[0-9]+",''.join(words))), end=" ")
    print()


