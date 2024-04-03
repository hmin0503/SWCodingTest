import sys
input = sys.stdin.readline

def dfs(V:list, st:int):
    # L 개의 문자로 구성
    if len(V) == L:
        # 최소 한 개의 자음을 가지고 두 개의 모음으로 구성
        # 교집합을 활용하여 자음 및 모음 개수 확인하기
				# 처음부터 V를 set로 지정하면, 원소의 순서가 바뀌기 때문에 X
        if len(set(V).intersection(cond1)) > 0 and len(set(V).intersection(cond2)) > 1:
            print(''.join(V))
            return
	
    for i in range(st, C): # 중복이 없기 때문에 시작 지점 지정하기
        if words[i] not in V:
            V.append(words[i])
            dfs(V, i+1)
            V.pop()

L, C = map(int, input().strip().split())
words = sorted(list(map(str, input().strip().split())))

# 조건: 최소 한 개의 모음 (aeiou) 과 최소 두 개의 자음으로 구성!
cond1 = set(list('aeiou'))
cond2 = set(list('bcdfghjklmnpqrstuvwxyz'))

dfs([], 0)