import sys
from math import ceil
input = sys.stdin.readline

def solution(N, A, B, C):
    answer = N # 시험장 마다 필수적으로 총감독이 필요
    # 총감독이 감독 가능한 응시자 수를 제외한 수 만큼 부감독 고용
    for a in A: 
        if a - B > 0: # 총감독으로 전체 시험장을 감독할수 없는 경우 부감독 고용 
            answer += ceil((a-B)/C) # 시험장 마다 필요한 부감독 수 구하기
    return answer
if __name__ == '__main__':
    # 1. 입력 값 받기
    N = int(input()) # 총 시험장 개수
    A = list(map(int, input().split())) # N개 시험장 각 응시자 수
    B, C = map(int, input().split()) # B 와 C
    print(solution(N, A, B, C))
