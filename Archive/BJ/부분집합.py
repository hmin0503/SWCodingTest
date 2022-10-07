arr = [1,2,3]
# 모든 비트의 경우의 수를 구하여 부분집합 구하기.
# 원소가 3개인 경우 -> 000 001 010 011 100 101 110 111
answers = []
for i in range(1<<len(arr)): # 공집합 제외, 부분집합 개수만큼 루프.
    # i가 0이면 000, 1이면 001, 2라면 010, --> 각 숫자를 이진수로 바꾸면 각 자리수 번호가 있다는 것을 의미.
    s = []
    for j in range(len(arr)): # i를 이진수로 바꿨을 때, 어느 자리수가 1인지 확인하는 과정.
        if i & (1<<j):
            s.append(arr[-(j+1)])
    answers.append(sorted(s))


arr = [1,2,3]
subsets = [[]] # 공집합 포함
for a in arr:
    s = len(subsets)
    for b in range(s):
        subsets.append(subsets[b]+[a])
    print(subsets)
