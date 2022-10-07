#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Stack #Silver4
# https://www.acmicpc.net/problem/4949
#------------------------

def main():
    while True:
        string = input().rstrip()
        if string == ".":
            break
        
        stack = []
        answer = "yes"
        for p in string:
            if p == ".":
                break

            if p == "(" or p == "[":
                stack.append(p)

            elif p == ")" or p == "]":
                if stack:
                    s = stack.pop()
                    if p == ")" and s == "[":
                        answer = "no"
                        break
                    if p == "]"  and s == "(":
                        answer = "no"
                        break
                else:
                    answer = "no"
        # loop문이 끝났을 때, stack은 비어 있어야 하나, 그렇지 않다면 잘못된 괄호 문자열.
        if stack:
            answer = "no"
        print(answer)

if __name__ == '__main__':
    main()