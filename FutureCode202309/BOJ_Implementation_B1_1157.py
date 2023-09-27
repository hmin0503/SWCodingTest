import sys
from collections import Counter
input = sys.stdin.readline

def solution(s):
    
    s = s.upper() # 모든 문자 대문자로 바꾸기
    word_dict = sorted(Counter(s).items(), key = lambda x: x[1], reverse = True) # 문자열 개수 세기 
    
    if len(word_dict) == 1: # 문자 종류가 1개면 return
        answer = word_dict[0][0]
    else:    # 문자 종류가 2개 이상이면 문자열 개수 비교 후 return
        if word_dict[0][1] > word_dict[1][1]:
            answer = word_dict[0][0]
        else:
            answer = "?"
    return answer

if __name__ == '__main__':
    s = input().strip()
    print(solution(s))
