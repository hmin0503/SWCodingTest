#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Stack #Silver4
# https://www.acmicpc.net/problem/9012
#------------------------

def main():
    import sys
    N = int(input())
    for _ in range(N):
        # n = int(sys.stdin.readline().rstrip())
        ps = list(input())
        stack = []
        answer = "YES"
        for p in ps:
            if p == "(":
                stack.append(p)
            else:
                if stack:
                    stack.pop()
                else:
                    answer = "NO"
                    break
        # loop문이 끝났을 때, stack은 비어 있어야 하나, 그렇지 않다면 잘못된 괄호 문자열.
        if stack:
            answer = "NO"
        print(answer)
if __name__ == '__main__':
    main()