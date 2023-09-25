#------------------------
# # Math
# https://school.programmers.co.kr/learn/courses/30/lessons/12953
#------------------------

def solution(arr):
    # 작은 수 부터 최대공배수 구하기.
    arr = sorted(arr)
    LCM = arr[0]
    for i in range(1, len(arr)):
        a, b = LCM, arr[i]
        while b > 0:
            a, b = b, a % b
        GCD = a
        LCM = (LCM*arr[i])//GCD
    return LCM