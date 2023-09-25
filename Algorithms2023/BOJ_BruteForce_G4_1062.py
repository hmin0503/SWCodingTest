# # 글자만 가르침.
# # 무얼 가르쳐야 할까
# # anta ~ tica

# N, K = map(int, input().split())
# alpha = {}
# for i in range(N):
#     word = input()
#     for w in word:
#         if w not in alpha:
#             alpha[w] = []
#             alpha[w].append(word)
#         else:
#             if word not in alpha[w]:
#                 alpha[w].append(word)
# alpha = sorted(alpha.items(), key = lambda x : len(x[1]), reverse=True)
# print(len(alpha[K-1][1]))

from sys import stdin
from itertools import combinations

def main():
    def input():
        return stdin.readline().rstrip()

    n, k = map(int,input().split())
    words = [set(input()).difference('a','c','i','t','n') for _ in range(n)]

    if k < 5:
        print(0)
        return

    letters = {chr(i+97): i for i in range(26)}
    ids = [i for i in range(26) if chr(i+97) not in ['a','c','i','t','n']]

    k -= 5
    res = 0
    for comb in combinations(ids,k):
        mask = 0
        for move in comb:
            mask |= 1 << move
            print(move, mask)
        
        cnt = 0
        for word in words:
            wordbit = 0
            for char in word:
                wordbit |= 1 << letters[char]
                print(word, char, letters[char], wordbit)
            if mask | wordbit == mask:
                cnt += 1

        res = max(cnt, res)
if __name__ == "__main__":
   main()