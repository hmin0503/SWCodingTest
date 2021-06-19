# 리스트의 인덱스 함수를 이용하여 반복하여 다음 1과 0의 위치를 찾아서 반환 후 리스트를 잘라가면서 
# 1이 연속적으로 있는 그룹 수 및 0이 연속적으로 있는 그룹 수를 구한 뒤 작은 값을 반환
def solution(number):
    number = list(map(int, list(number)))
    num0 = 0
    num1 = 1
    while True:
        if number[0] == 0:
            try:
                idx = number.index(1)
                num0 += 1
                number = number[idx:]
            except ValueError:
                break
        else :
            try:
                idx = number.index(0)
                num1 += 1
                number = number[idx:]
            except ValueError:
                break
    return min(num0, num1)
    
# %%
print(solution("0001100")) # 1
print(solution("000110011")) # 2
print(solution("0101000111")) # 3
