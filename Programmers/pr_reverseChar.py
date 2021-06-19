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
