###########################################################################
"""
5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2
"""
###########################################################################


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = float(input())
    result = ""
    i = 1
    while True:
        if i >= 13:
            print("#{} overflow".format(test_case))
            break
        num *= 2
        if num == 1:
            result += "1"
            print("#{} {}".format(test_case, result))
            break
        elif num > 1:
            num -= 1
            result += "1"
        else:
            result += "0"
        i += 1
